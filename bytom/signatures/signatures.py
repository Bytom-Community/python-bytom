#!/usr/bin/env python
# coding=utf-8

import copy
import simplejson
from binascii import hexlify
from binascii import unhexlify
from bytom.signatures import utils
from bytom.signatures.signer import Signer
from bytom.signatures.finddst import FindDst
from bytom.signatures.nonhardenedchild import NonHardenedChild
from bytom.signatures.derivexpub import DeriveXpub
from bytom.signatures.expandedprivatekey import ExpandedPrivateKey

class Signatures(object):

    @classmethod
    def generate_signatures(cls, private_keys, input_template, input_decoded_tx):
        if type(input_template) != dict:
            template = simplejson.loads(simplejson.dumps(input_template))
        else:
            template = copy.deepcopy(input_template)

        if type(input_decoded_tx) != dict:
            decoded_tx = simplejson.loads(simplejson.dumps(input_decoded_tx))
        else:
            decoded_tx = copy.deepcopy(input_decoded_tx)
            
        result = copy.deepcopy(template)

        for i, signing in enumerate(template["signing_instructions"]):
            for wc in signing["witness_components"]:
                # Have two cases
                if wc["type"] == "raw_tx_signature":
                    if wc["signatures"] is None or len(wc["signatures"]) < len(wc["keys"]):
                        wc["signatures"] = ["" for i in range(0, len(wc["keys"]))]
    
                    input_id = decoded_tx["inputs"][signing["position"]]["input_id"]
                    tx_id = decoded_tx["tx_id"]
                    message = utils.sha3_digest_256(unhexlify(input_id + tx_id))
    
                    for j, key in enumerate(wc["keys"]):
                        if wc["signatures"][j] is None or wc["signatures"][j] == "":
                            public_key = key["xpub"]
                            dst = FindDst.find_dist(private_keys, public_key)
                            private_key = unhexlify(private_keys[dst])
                            hpaths = key["derivation_path"]
                            child_xprv = NonHardenedChild.child(private_key, hpaths)
                            xpub = DeriveXpub.derive_xpub(private_key)
                            expanded_prv = ExpandedPrivateKey.expanded_private_key(child_xprv)

                            print("private_key: %s" % hexlify(private_key))
                            print("child_xprv: %s" % hexlify(child_xprv))
                            print("xpub: %s" % hexlify(xpub))
                            print("message: %s" % hexlify(message))

                            sig = Signer.ed25519_inner_sign(expanded_prv, message)
                            
                            print("sig: %s" % hexlify(sig))
                            wc["signatures"][j] = hexlify(sig)
                            result["signing_instructions"][i]["witness_components"][j]["signatures"] = wc["signatures"]
                    break
                elif wc.type == "":
                    break
                else:
                    continue

        return result
