#!/usr/bin/env python
# coding=utf-8

import six
import hmac
import hashlib
import sha3
from binascii import hexlify
from binascii import unhexlify
from bytom.signatures import ed25519

if six.PY3:
    def byte2int(b):
        return b
    def int2byte(i):
        return bytes(chr(i % 256), encoding="UTF-8")

elif six.PY2:
    def byte2int(b):
        return ord(b)
    def int2byte(i):
        return chr(i % 256)

L = 2 ** 252 + 27742317777372353535851937790883648493

def sha3_digest_256(data):
    s = sha3.sha3_256()
    s.update(data)
    return s.digest()

def hmac_sha_512(data, key):
    digest = hmac.new(key, msg=data, digestmod=hashlib.sha512).digest()
    return digest

def sha_512(data):
    md = hashlib.sha512()
    md.update(data)
    return md.digest()

def hex2int(hex):
    ## converts a hex string to integer
    unhex = unhexlify(hex)
    s = 0
    for i in range(len(unhex)):
        s += 256 ** i * byte2int(unhex[i])
    return s

def int2hex(int):
    ## converts an integer to a little endian encoded hex string
    return hexlify(ed25519.encodeint(int))

def sc_reduce32(input):
    ## convert hex string input to integer
    int = hex2int(input)
    ## reduce mod l
    modulo = int % L
    ## convert back to hex string for return value
    return int2hex(modulo)

def sc_muladd(a, b, c):
    a_int = hex2int(a)
    b_int = hex2int(b)
    c_int = hex2int(c)
    
    s = a_int * b_int + c_int
    modulo = s % L
    return int2hex(modulo)
