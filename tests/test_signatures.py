#!/usr/bin/env python
# coding=utf-8

import simplejson
from bytom.client import BytomAPI
from bytom.models import APIModel
from bytom.signatures import Signatures

api = BytomAPI()

def test_sign_use_template_dictionary():
    privates = ["10fdbc41a4d3b8e5a0f50dd3905c1660e7476d4db3dbd9454fa4347500a633531c487e8174ffc0cfa76c3be6833111a9b8cd94446e37a76ee18bb21a7d6ea66b"]
    raw_tx = "0701dfd5c8d505010161015f0434bc790dbb3746c88fd301b9839a0f7c990bb8bdc96881d17bc2fb47525ad8ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80d0dbc3f4020101160014f54622eeb837e39d359f7530b6fbbd7256c9e73d010002013effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8c98d2b0f402011600144453a011caf735428d0291d82b186e976e286fc100013afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff40301160014613908c28df499e3aa04e033100efaa24ca8fd0100"
    raw_transaction = api.decode_raw_transaction(raw_tx)

    dictionary = {
        "raw_transaction": "0701dfd5c8d505010161015f0434bc790dbb3746c88fd301b9839a0f7c990bb8bdc96881d17bc2fb47525ad8ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff80d0dbc3f4020101160014f54622eeb837e39d359f7530b6fbbd7256c9e73d010002013effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8c98d2b0f402011600144453a011caf735428d0291d82b186e976e286fc100013afffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff40301160014613908c28df499e3aa04e033100efaa24ca8fd0100",
        "signing_instructions": [
            {
                "position": 0,
                "witness_components": [
                    {
                        "type": "raw_tx_signature",
                        "quorum": 1,
                        "keys": [
                            {
                                "xpub": "d9c7b41f030a398dada343096040c675be48278046623849977cb0fd01d395a51c487e8174ffc0cfa76c3be6833111a9b8cd94446e37a76ee18bb21a7d6ea66b",
                                "derivation_path": ["010400000000000000", "0100000000000000"],
                            },
                        ],
                        "signatures": None,
                    },
                    {
                        "type": "data", 
                        "value": "5024b9d7cdfe9b3ece98bc06111e06dd79d425411614bfbb473d07ca44795612",
                        "quorum": 0,
                    },
                ],
            },
        ],
        "allow_additional_actions": False,
    }
    template = APIModel(dictionary).object_from_dictionary()
    result = Signatures.generate_signatures(privates, template, raw_transaction)
    print(result)

def test_sign_single_key():
    asset_id = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
    address = "sm1qvyus3s5d7jv782syuqe3qrh65fx23lgpzf33em"
    actions = [
        {
          "account_id": "0G0NLBNU00A02",
          "amount": 40000000,
          "asset_id": asset_id,
          "type": "spend_account"
        },
        {
          "account_id": "0G0NLBNU00A02",
          "amount": 300000000,
          "asset_id": asset_id,
          "type": "spend_account"
        },
        {
          "amount": 30000000,
          "asset_id": asset_id,
          "address": address,
          "type": "control_address"
        }
    ]
    template = api.build_transaction(base_transaction=None, actions=actions, ttl=0, time_range=1521625823, return_json=True)
    print("template: " + str(template))
    decoded_tx = api.decode_raw_transaction(template["raw_transaction"], return_json=True)
    print("decoded_tx: " + str(decoded_tx))
    private_keys = ["10fdbc41a4d3b8e5a0f50dd3905c1660e7476d4db3dbd9454fa4347500a633531c487e8174ffc0cfa76c3be6833111a9b8cd94446e37a76ee18bb21a7d6ea66b"]
    print("private_keys: " + str(private_keys))
    basic_signed = Signatures.generate_signatures(private_keys, template, decoded_tx)
    print("basic_signed: " + str(basic_signed))
    result = api.sign_transaction("", basic_signed, return_json=True)
    print("result raw_transaction: " + str(result))


def test_sign_multi_keys():
    asset_id = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
    address = "sm1qvyus3s5d7jv782syuqe3qrh65fx23lgpzf33em"
    actions = [
        {
          "account_id": "0G1RPP6OG0A06",
          "amount": 40000000,
          "asset_id": asset_id,
          "type": "spend_account"
        },
        {
          "account_id": "0G1RPP6OG0A06",
          "amount": 300000000,
          "asset_id": asset_id,
          "type": "spend_account"
        },
        {
          "amount": 30000000,
          "asset_id": asset_id,
          "address": address,
          "type": "control_address"
        }
    ]
    template = api.build_transaction(base_transaction=None, actions=actions, ttl=10, time_range=1521625823, return_json=True)
    print("template: " + str(template))
    decoded_tx = api.decode_raw_transaction(template["raw_transaction"], return_json=True)
    print("decoded_tx: " + str(decoded_tx))
    private_keys = ["08bdbd6c22856c5747c930f64d0e5d58ded17c4473910c6c0c3f94e485833a436247976253c8e29e961041ad8dfad9309744255364323163837cbef2483b4f67", 
                    "40c821f736f60805ad59b1fea158762fa6355e258601dfb49dda6f672092ae5adf072d5cab2ceaaa0d68dd3fe7fa04869d95afed8c20069f446a338576901e1b"]
    print("private_keys: " + str(private_keys))
    basic_signed = Signatures.generate_signatures(private_keys, template, decoded_tx)
    print("basic_signed: " + str(basic_signed))
    result = api.sign_transaction("", basic_signed, return_json=True)
    print("result raw_transaction: " + str(result))

def test_sign_multi_keys_multi_inputs():
    asset_id = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
    address = "sm1qvyus3s5d7jv782syuqe3qrh65fx23lgpzf33em"
    actions = [
        {
          "account_id": "0G1RPP6OG0A06",
          "amount": 40000000,
          "asset_id": asset_id,
          "type": "spend_account"
        },
        {
          "account_id": "0G1RPP6OG0A06",
          "amount": 300000000,
          "asset_id": asset_id,
          "type": "spend_account"
        },
        {
          "account_id": "0G1Q6V1P00A02",
          "amount": 40000000,
          "asset_id": asset_id,
          "type": "spend_account"
        },
        {
          "account_id": "0G1Q6V1P00A02",
          "amount": 300000000,
          "asset_id": asset_id,
          "type": "spend_account"
        },
        {
          "amount": 60000000,
          "asset_id": asset_id,
          "address": address,
          "type": "control_address"
        }
    ]
    template = api.build_transaction(base_transaction=None, actions=actions, ttl=10, time_range=1521625823, return_json=True)
    print("template: " + str(template))
    decoded_tx = api.decode_raw_transaction(template["raw_transaction"], return_json=True)
    print("decoded_tx: " + str(decoded_tx))
    private_keys = ["08bdbd6c22856c5747c930f64d0e5d58ded17c4473910c6c0c3f94e485833a436247976253c8e29e961041ad8dfad9309744255364323163837cbef2483b4f67", 
                    "40c821f736f60805ad59b1fea158762fa6355e258601dfb49dda6f672092ae5adf072d5cab2ceaaa0d68dd3fe7fa04869d95afed8c20069f446a338576901e1b",
                    "08bdbd6c22856c5747c930f64d0e5d58ded17c4473910c6c0c3f94e485833a436247976253c8e29e961041ad8dfad9309744255364323163837cbef2483b4f67"]
    print("private_keys: " + str(private_keys))
    basic_signed = Signatures.generate_signatures(private_keys, template, decoded_tx)
    print("basic_signed: " + str(basic_signed))
    result = api.sign_transaction("", basic_signed, return_json=True)
    print("result raw_transaction: " + str(result))

