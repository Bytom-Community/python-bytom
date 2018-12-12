#!/usr/bin/env python
# coding=utf-8

from .bind import bind_method

NO_ACCEPT_PARAMETERS = []

class BytomAPI(object):
    default_url = "http://localhost:9888"
    api_name = "Bytom"
    version = "1.0.3"

    def __init__(self, url=default_url, access_token=""):
        self.url = url
        self.access_token = access_token
        self.auth = ()
        if self.access_token != "":
            self.auth = tuple(self.access_token.split(":"))

    # Available with wallet enable
    create_key = bind_method(
                path="/create-key",
                accepts_parameters=["alias", "password", "language", "mnemonic"])

    list_keys = bind_method(
                path="/list-keys",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    delete_key = bind_method(
                path="/delete-key",
                accepts_parameters=["xpub", "password"])

    check_key_password = bind_method(
                path="/check-key-password",
                accepts_parameters=["xpub", "password"])

    reset_key_password = bind_method(
                path="/reset-key-password",
                accepts_parameters=["xpub", "old_password", "new_password"])

    create_account = bind_method(
                path="/create-account",
                accepts_parameters=["root_xpubs", "alias", "quorum", "access_token"])

    list_accounts = bind_method(
                path="/list-accounts",
                accepts_parameters=["id", "alias"])

    delete_account = bind_method(
                path="/delete-account",
                accepts_parameters=["account_info"])

    create_account_receiver = bind_method(
                path="/create-account-receiver",
                accepts_parameters=["account_alias", "account_id"])

    list_addresses = bind_method(
                path="/list-addresses",
                accepts_parameters=["account_alias", "account_id", "from", "count"])

    validate_address = bind_method(
                path="/validate-address",
                accepts_parameters=["address"])

    get_mining_address = bind_method(
                path="/get-mining-address",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    set_mining_address = bind_method(
                path="/set-mining-address",
                accepts_parameters=["mining_address"])

    get_coinbase_arbitrary = bind_method(
                path="/get-coinbase-arbitrary",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    set_coinbase_arbitrary = bind_method(
                path="/set-coinbase-arbitrary",
                accepts_parameters=["arbitrary"])

    list_pubkeys = bind_method(
                path="/list-pubkeys",
                accepts_parameters=["account_alias", "account_id", "public_key"])

    create_asset = bind_method(
                path="/create-asset",
                accepts_parameters=["alias", "definition", "root_xpubs", "quorum", "issuance_program"])

    get_asset = bind_method(
                path="/get-asset",
                accepts_parameters=["id"])

    list_assets = bind_method(
                path="/list-assets",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    update_asset_alias = bind_method(
                path="/update-asset-alias",
                accepts_parameters=["id", "alias"])

    list_balances = bind_method(
                path="/list-balances",
                accepts_parameters=["account_id", "account_alias"])

    list_unspent_outputs = bind_method(
                path="/list-unspent-outputs",
                accepts_parameters=["id", "unconfirmed", "smart_contract", "from", "count", "account_id", "account_alias"])

    backup_wallet = bind_method(
                path="/backup-wallet",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    restore_wallet = bind_method(
                path="/restore-wallet",
                accepts_parameters=["account_image", "asset_image", "key_images"])

    rescan_wallet = bind_method(
                path="/rescan-wallet",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    wallet_info = bind_method(
                path="/wallet-info",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    sign_message = bind_method(
                path="/sign-message",
                accepts_parameters=["address", "message", "password"])

    decode_program = bind_method(
                path="/decode-program",
                accepts_parameters=["program"])

    get_transaction = bind_method(
                path="/get-transaction",
                accepts_parameters=["tx_id"])

    list_transactions = bind_method(
                path="/list-transactions",
                accepts_parameters=["id", "account_id", "detail", "unconfirmed", "from", "count"])

    build_transaction = bind_method(
                path="/build-transaction",
                accepts_parameters=["base_transaction", "ttl", "time_range", "actions"])

    build_chain_transactions = bind_method(
                path="/build-chain-transactions",
                accepts_parameters=["base_transaction", "ttl", "time_range", "actions"])

    sign_transaction = bind_method(
                path="/sign-transaction",
                accepts_parameters=["password", "transaction"])

    sign_transactions = bind_method(
                path="/sign-transactions",
                accepts_parameters=["password", "transaction"])

    # Available whether or not the wallet is open
    submit_transaction = bind_method(
                path="/submit-transaction",
                accepts_parameters=["raw_transaction"])

    submit_transactions = bind_method(
                path="/submit-transactions",
                accepts_parameters=["raw_transactions"])

    estimate_transaction_gas = bind_method(
                path="/estimate-transaction-gas",
                accepts_parameters=["transaction_template"])

    create_access_token = bind_method(
                path="/create-access-token",
                accepts_parameters=["id", "type"])

    list_access_tokens = bind_method(
                path="/list-access-tokens",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    delete_access_token = bind_method(
                path="/delete-access-token",
                accepts_parameters=["id"])

    check_access_token = bind_method(
                path="/check-access-token",
                accepts_parameters=["id", "secret"])

    create_transaction_feed = bind_method(
                path="/create-transaction-feed",
                accepts_parameters=["alias", "filter"])

    get_transaction_feed = bind_method(
                path="/get-transaction-feed",
                accepts_parameters=["alias"])

    list_transaction_feeds = bind_method(
                path="/list-transaction-feeds",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    delete_transaction_feed = bind_method(
                path="/delete-transaction-feed",
                accepts_parameters=["alias"])

    update_transaction_feed = bind_method(
                path="/update-transaction-feed",
                accepts_parameters=["alias", "filter"])

    get_unconfirmed_transaction = bind_method(
                path="/get-unconfirmed-transaction",
                accepts_parameters=["tx_id"])

    list_unconfirmed_transactions = bind_method(
                path="/list-unconfirmed-transactions",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    decode_raw_transaction = bind_method(
                path="/decode-raw-transaction",
                accepts_parameters=["raw_transaction"])

    get_block_count = bind_method(
                path="/get-block-count",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    get_block_hash = bind_method(
                path="/get-block-hash",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    get_block = bind_method(
                path="/get-block",
                accepts_parameters=["block_height", "block_hash"])

    get_block_header = bind_method(
                path="/get-block-header",
                accepts_parameters=["block_height", "block_hash"])

    get_difficulty = bind_method(
                path="/get-difficulty",
                accepts_parameters=["block_height", "block_hash"])

    get_hash_rate = bind_method(
                path="/get-hash-rate",
                accepts_parameters=["block_height", "block_hash"])

    net_info = bind_method(
                path="/net-info",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    is_mining = bind_method(
                path="/is-mining",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    set_mining = bind_method(
                path="/set-mining",
                accepts_parameters=["is_mining"])

    gas_rate = bind_method(
                path="/gas-rate",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    verify_message = bind_method(
                path="/verify-message",
                accepts_parameters=["address", "derived_xpub", "message", "signature"])

    compile = bind_method(
                path="/compile",
                accepts_parameters=["contract", "args"])

    list_peers = bind_method(
                path="/list-peers",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    disconnect_peer = bind_method(
                path="/disconnect-peer",
                accepts_parameters=["peer_id"])

    connect_peer = bind_method(
                path="/connect-peer",
                accepts_parameters=["ip", "port"])

    get_work = bind_method(
                path="/get-work",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    submit_work = bind_method(
                path="/submit-work",
                accepts_parameters=["block_header"])

    get_work_json = bind_method(
                path="/get-work-json",
                accepts_parameters=NO_ACCEPT_PARAMETERS)

    submit_work_json = bind_method(
                path="/submit-work-json",
                accepts_parameters=["block_header"])

