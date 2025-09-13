from hyperliquid.exchange import Exchange
import utils
from hyperliquid.utils import constants
from hyperliquid.info import Info

CONTRACT = "0x58CB3Be409145bf92af7C03A02c9e45683A51620"


def main():
    address, info, exchange = utils.setup(
        constants.MAINNET_API_URL, skip_ws=True)
    exchange = Exchange(exchange.wallet, exchange.base_url,
                        vault_address=CONTRACT)
    result = exchange.update_leverage(10, "ETH")
    print(result)


if __name__ == "__main__":
    main()
