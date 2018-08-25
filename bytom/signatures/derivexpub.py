#!/usr/bin/env python
# coding=utf-8

from bytom.signatures import ed25519

class DeriveXpub(object):

    @classmethod
    def derive_xpub(cls, xprv):
        scalar = ed25519.decodeint(xprv[:len(xprv)//2])
        buf = ed25519.encodepoint(ed25519.scalarmultbase(scalar))
        xpub = buf + xprv[len(xprv)//2:]
        return xpub

