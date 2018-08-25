#!/usr/bin/env python
# coding=utf-8

from binascii import hexlify
from binascii import unhexlify
from bytom.signatures.derivexpub import DeriveXpub

class FindDst(object):

    @classmethod
    def find_dist(cls, private_keys, xpub):
        dst = -1
        for i, key in enumerate(private_keys):
            temp_xpub = DeriveXpub.derive_xpub(unhexlify(key))
            if xpub == hexlify(temp_xpub).decode():
                dst = i
                print("private[dst]: %s", private_keys[dst])
                break
    
        if dst == -1:
            raise Exception("Not a proper private key to sign transaction.")
        
        return dst

