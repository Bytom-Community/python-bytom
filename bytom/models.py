#!/usr/bin/env python
# coding=utf-8

import six
import simplejson
from collections import namedtuple

class APIModel(object):
    
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.data = simplejson.dumps(dictionary)

    def object_from_dictionary(self):
        if self.dictionary == "" or self.dictionary == {}:
            return None

        return simplejson.loads(self.data, object_hook=lambda d: namedtuple('Object', d.keys())(*d.values()))

    def __repr__(self):
        return str(self)

    def __str__(self):
        if six.PY3:
            return self.__unicode__()
        else:
            return unicode(self).encode('utf-8')

    def __unicode__(self):
        return "APIModel"
