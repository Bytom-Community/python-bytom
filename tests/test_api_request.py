#!/usr/bin/env python
# coding=utf-8

from bytom.client import BytomAPI
from bytom.bind import BytomClientError, BytomAPIError
import pytest
import requests_mock
import simplejson

api = BytomAPI()

def test_invalid_json():
    """Test Invalid response error"""

    with pytest.raises(BytomClientError):
        with requests_mock.mock() as m:
            not_json_str = "<html><body>Error</body></html>"
            m.register_uri('POST', "http://localhost:9888/list-keys", text=not_json_str)
            api.list_keys()

def test_api_error():
    """Test API response error"""
    
    with pytest.raises(BytomAPIError):
        with requests_mock.mock() as m:
            json_obj = {"code": "BTM002","msg":"Invalid request body","status":"fail", "temporary": False, "detail": "bad key string: bad key string"}
            m.register_uri('POST', "http://localhost:9888/delete-key", json=json_obj) 
            api.delete_key("123", "456")

def test_success():
    """Test API success"""

    with requests_mock.mock() as m:
        json_obj = {"status": "success", "data": {"best_block_height": 76251, "wallet_height": 76251}}
        m.register_uri('POST', "http://localhost:9888/wallet-info", json=json_obj)
        ret = api.wallet_info()

    assert ret.best_block_height == 76251
    assert ret.wallet_height == 76251

def test_return_json():
    """Test return_json"""

    with requests_mock.mock() as m:
        json_obj = {"status": "success", "data": {"listening": True, "syncing": False, "mining": False, "peer_count": 3, "current_block": 76252, "highest_block": 76252, "network_id": "mainnet", "version": "1.0.4-90825109"}}
        m.register_uri('POST', "http://localhost:9888/net-info", json=json_obj)
        ret = api.net_info(return_json=True)

    assert ret["mining"] is False
    assert ret["peer_count"] == 3
