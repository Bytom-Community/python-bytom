#!/usr/bin/env python
# coding=utf-8

import six
import simplejson
from .rpc import RPCRequest
from .models import APIModel

class BytomClientError(Exception):
    def __init__(self, error_message, status_code=None):
        self.status_code = status_code
        self.error_message = error_message

    def __str__(self):
        if self.status_code:
            return "(%s) %s" % (self.status_code, self.error_message)
        else:
            return self.error_message

class BytomAPIError(Exception):

    def __init__(self, status_code, error_message, error):
        self.status_code = status_code
        self.error_message = error_message
        self.error = error

    def __str__(self):
        return "(%s) %s" % (self.status_code, self.error)

def bind_method(**config):

    class BytomAPIMethod(object):
        path = config['path']
        accepts_parameters = config.get("accepts_parameters", [])

        def __init__(self, api, *args, **kwargs):
            self.api = api
            self.return_json = kwargs.pop("return_json", False)
            self.return_dict = kwargs.pop("return_dict", False)
            self.parameters = {}
            self._build_parameters(args, kwargs)

        def _build_parameters(self, args, kwargs):
            for index, value in enumerate(args):
                if value is None:
                    continue

                try:
                    self.parameters[self.accepts_parameters[index]] = value
                except IndexError:
                    raise BytomClientError("Too many arguments supplied") 

            for key, value in six.iteritems(kwargs):
                if value is None:
                    continue

                if key in self.parameters:
                    raise BytomClientError("Parameter %s already supplied" % key)
                self.parameters[key] = value

        def _do_api_request(self, url, body=None, headers=None):
            response = RPCRequest(self.api).make_request(url, body=body, headers=headers)
            try:
                api_ret = response.json()
            except ValueError:
                raise BytomClientError('Unable to parse response, not valid JSON.', status_code=response.status_code)

            if api_ret["status"] == "fail":
                raise BytomAPIError(api_ret.get("code", ""), api_ret.get("msg", ""), api_ret)

            data = api_ret.get("data", {})

            if self.return_json:
                return simplejson.dumps(data)
            elif self.return_dict:
                return data
            else:
                return APIModel(data).object_from_dictionary()

        def execute(self):
            url, body, headers = RPCRequest(self.api).prepare_request(self.path, self.parameters)
            content = self._do_api_request(url, body, headers)
            return content

    def _call(api, *args, **kwargs):
        method = BytomAPIMethod(api, *args, **kwargs)
        return method.execute()

    return _call
