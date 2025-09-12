from hyperliquid.exchange import Exchange
import utils
from hyperliquid.utils import constants
from hyperliquid.info import Info

CONTRACT = "0xe8475439795725172b77dBFB9b659E03Cd7Fb0EB"


def main():
    address, info, exchange = utils.setup(
        constants.MAINNET_API_URL, skip_ws=True)
    exchange = Exchange(exchange.wallet, exchange.base_url,
                        vault_address=CONTRACT)
    exchange.update_leverage(10, "ETH")


if __name__ == "__main__":
    main()
