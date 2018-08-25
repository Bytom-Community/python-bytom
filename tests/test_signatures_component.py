#!/usr/bin/env python
# coding=utf-8

from bytom.signatures.derivexpub import DeriveXpub
from bytom.signatures.nonhardenedchild import NonHardenedChild
from bytom.signatures.expandedprivatekey import ExpandedPrivateKey
from bytom.signatures.signer import Signer
from binascii import unhexlify
from binascii import hexlify

def test_derive_xpub():
    hxprv = "10fdbc41a4d3b8e5a0f50dd3905c1660e7476d4db3dbd9454fa4347500a633531c487e8174ffc0cfa76c3be6833111a9b8cd94446e37a76ee18bb21a7d6ea66b"
    xpub = DeriveXpub.derive_xpub(unhexlify(hxprv))
    assert "d9c7b41f030a398dada343096040c675be48278046623849977cb0fd01d395a51c487e8174ffc0cfa76c3be6833111a9b8cd94446e37a76ee18bb21a7d6ea66b" == hexlify(xpub).decode()

def test_nh_child():
    hxprv = "10fdbc41a4d3b8e5a0f50dd3905c1660e7476d4db3dbd9454fa4347500a633531c487e8174ffc0cfa76c3be6833111a9b8cd94446e37a76ee18bb21a7d6ea66b"
    xprv = unhexlify(hxprv)
    hpaths = ["010400000000000000", "0100000000000000"]
    paths = [unhexlify(hpaths[0]), unhexlify(hpaths[1])]
    res = xprv
    for i in range(0, len(hpaths)):
        xpub = DeriveXpub.derive_xpub(res)
        res = NonHardenedChild.nh_child(paths[i], res, xpub)
    assert "e8c0965af60563c4cabcf2e947b1cd955c4f501eb946ffc8c3447e5ec8a6335398a3720b3f96077fa187fdde48fe7dc293984b196f5e292ef8ed78fdbd8ed954" == hexlify(res).decode()

def test_child():
    hxprv = "10fdbc41a4d3b8e5a0f50dd3905c1660e7476d4db3dbd9454fa4347500a633531c487e8174ffc0cfa76c3be6833111a9b8cd94446e37a76ee18bb21a7d6ea66b"
    hpaths = [u"010400000000000000", u"0100000000000000"]
    child_xprv = NonHardenedChild.child(unhexlify(hxprv), hpaths)
    assert "e8c0965af60563c4cabcf2e947b1cd955c4f501eb946ffc8c3447e5ec8a6335398a3720b3f96077fa187fdde48fe7dc293984b196f5e292ef8ed78fdbd8ed954" == hexlify(child_xprv).decode()

def test_expanded_key():
    child_xprv = "e8c0965af60563c4cabcf2e947b1cd955c4f501eb946ffc8c3447e5ec8a6335398a3720b3f96077fa187fdde48fe7dc293984b196f5e292ef8ed78fdbd8ed954"
    z = ExpandedPrivateKey.expanded_private_key(unhexlify(child_xprv))
    assert "e8c0965af60563c4cabcf2e947b1cd955c4f501eb946ffc8c3447e5ec8a633535b899d45316cd83e027913d3ff3dc52f6a951a686fd2b750099e1f7c70cb98c3" == hexlify(z).decode()

def test_signer():
    root_xprv = "10fdbc41a4d3b8e5a0f50dd3905c1660e7476d4db3dbd9454fa4347500a633531c487e8174ffc0cfa76c3be6833111a9b8cd94446e37a76ee18bb21a7d6ea66b"
    child_xprv = "e8c0965af60563c4cabcf2e947b1cd955c4f501eb946ffc8c3447e5ec8a6335398a3720b3f96077fa187fdde48fe7dc293984b196f5e292ef8ed78fdbd8ed954"
    expanded_xprv = "e8c0965af60563c4cabcf2e947b1cd955c4f501eb946ffc8c3447e5ec8a633535b899d45316cd83e027913d3ff3dc52f6a951a686fd2b750099e1f7c70cb98c3"
    hashed_message = "02eda3cd8d1b0efaf7382af6ea53a429ed3ed6042998d2b4a382575248ebc922"
    sig = Signer.ed25519_inner_sign(unhexlify(expanded_xprv), unhexlify(hashed_message))
    assert "38b11090e8dd5372018acc24ea4db2c3d82cf01ed5c69a0fae95bff2379c1630f8c8f96937b22685142b4181e6ef5072e7945c101eb81814a20d90cb1d1f0c08" == hexlify(sig).decode()
