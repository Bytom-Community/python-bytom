#!/usr/bin/env python
# coding=utf-8

from binascii import hexlify
from binascii import unhexlify
from bytom.signatures import utils
from bytom.signatures.derivexpub import DeriveXpub 

class NonHardenedChild(object):
    
    @classmethod
    def nh_child(cls, path, xprv, xpub):
        # begin build data
        data = b'N' + xpub[:len(xpub) // 2] + path
        
        # begin build key
        key = xpub[len(xpub) // 2:]

        # do HMAC-SHA512
        res = utils.hmac_sha_512(data, key)
        res = bytearray(res)

        # begin operate res[:32]
        f = res[:len(res) // 2]
        f = cls.prune_intermediate_scalar(f)
        res = f[:len(res)//2] + res[len(res)//2:]

        # begin operate res[:32] again
        carry = 0
        sum = 0
        for i in range(0, 32):
            xprv_int = utils.byte2int(xprv[i]) & 0xFF
            res_int = res[i] & 0xFF
            sum = xprv_int + res_int + carry
            res[i] = sum % 256
            carry = sum >> 8
        if (sum >> 8) != 0:
            print("sum does not fit in 256-bit int")

        return bytes(res)

    @classmethod
    def prune_intermediate_scalar(cls, f):
        f = bytearray(f)
        f[0] = f[0] & 248       # clear bottom 3 bits
        f[29] = f[29] & 1       # clear 7 high bits
        f[30] = 0               # clear 8 bits
        f[31] = 0               # clear 8 bits
        return f

    @classmethod
    def child(cls, xprv, hpaths):
        paths = [unhexlify(hpaths[0]), unhexlify(hpaths[1])]
        res = xprv
        for i in range(0, len(hpaths)):
            xpub = DeriveXpub.derive_xpub(res)
            res = cls.nh_child(paths[i], res, xpub)

        return res

