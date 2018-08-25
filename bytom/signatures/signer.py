#!/usr/bin/env python
# coding=utf-8

import hashlib
from binascii import hexlify
from binascii import unhexlify
from bytom.signatures import utils
from bytom.signatures import ed25519
from bytom.signatures.derivexpub import DeriveXpub

class Signer(object):

    @classmethod
    def ed25519_inner_sign(cls, private_key, message):
        digest_data = private_key[32:64] + message

        message_digest = utils.sha_512(digest_data)
        message_digest = utils.sc_reduce32(hexlify(message_digest))
        message_digest = unhexlify(message_digest)
        message_digest_reduced = message_digest[0:32]

        scalar = ed25519.decodeint(message_digest_reduced)
        encoded_r = ed25519.encodepoint(ed25519.scalarmultbase(scalar))
        public_key = DeriveXpub.derive_xpub(private_key)
        hram_digest_data = encoded_r + public_key[:32] + message

        hram_digest = utils.sha_512(hram_digest_data)
        hram_digest = utils.sc_reduce32(hexlify(hram_digest))
        hram_digest = unhexlify(hram_digest)
        hram_digest_reduced = hram_digest[0:32]

        sk = private_key[:32]
        s = utils.sc_muladd(hexlify(hram_digest_reduced), hexlify(sk), hexlify(message_digest_reduced))
        s = unhexlify(s)

        signature = encoded_r + s
        return signature
