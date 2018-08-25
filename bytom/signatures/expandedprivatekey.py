#!/usr/bin/env python
# coding=utf-8

from binascii import unhexlify
from bytom.signatures import utils

class ExpandedPrivateKey(object):

    @classmethod
    def expanded_private_key(cls, data):
        # "457870616e64" is "Expand" hex.
        res = utils.hmac_sha_512(data, unhexlify("457870616e64"))
        res = data[:32] + res[32:]

        return res

