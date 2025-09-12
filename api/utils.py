import json
import os

import eth_account
from eth_account.signers.local import LocalAccount
from dotenv import load_dotenv

from hyperliquid.exchange import Exchange
from hyperliquid.info import Info


def setup(base_url=None, skip_ws=False, perp_dexs=None):
    # Load environment variables from .env file
    load_dotenv()

    # Get private key from environment variable
    private_key = os.getenv("PRIVATE_KEY")
    if not private_key:
        raise ValueError("PRIVATE_KEY environment variable is not set")

    account: LocalAccount = eth_account.Account.from_key(private_key)

    # Get address from environment variable, fallback to account address if not set
    address = os.getenv("ADDRESS")
    if not address:
        address = account.address
    print("Running with account address:", address)
    if address != account.address:
        print("Running with agent address:", account.address)
    info = Info(base_url, skip_ws, perp_dexs=perp_dexs)
    user_state = info.user_state(address)
    spot_user_state = info.spot_user_state(address)
    margin_summary = user_state["marginSummary"]
    if float(margin_summary["accountValue"]) == 0 and len(spot_user_state["balances"]) == 0:
        print("Not running the example because the provided account has no equity.")
        url = info.base_url.split(".", 1)[1]
        error_string = f"No accountValue:\nIf you think this is a mistake, make sure that {address} has a balance on {url}.\nIf address shown is your API wallet address, update the config to specify the address of your account, not the address of the API wallet."
        raise Exception(error_string)
    exchange = Exchange(account, base_url,
                        account_address=address, perp_dexs=perp_dexs)
    return address, info, exchange
