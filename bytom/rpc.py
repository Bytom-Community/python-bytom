#!/usr/bin/env python
# coding=utf-8

import requests
import simplejson

class RPCRequest(object):
    def __init__(self, api):
        self.api = api

    def _get_base_path(self, path):
        return self.api.base_path

    def _full_url(self, path):
        return "%s%s" % (self.api.url, path) 

    def _post_body(self, params):
        body = simplejson.dumps(params)
        return body

    def prepare_request(self, path, params):
        headers = {}

        url = self._full_url(path) 
        body = self._post_body(params)

        return url, body, headers

    def make_request(self, url, body=None, headers=None):
        headers = headers or {}
        if 'User-Agent' not in headers:
            headers.update({"User-Agent": "%s Python Client - %s" % (self.api.api_name, self.api.version)})
        if 'Content-Type' not in headers:
            headers.update({"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"})
        return requests.post(url, data=body, headers=headers, auth=self.api.auth)

