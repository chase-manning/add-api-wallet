# Add API Wallet

This is a repo to help replicate the issue with have with the Add API Wallet function in CoreWriter. It consists of:

- A simple smart contract to call the Add API Wallet action
- A simple script to deploy the contract and call the Add API Wallet action
- A simple Python script to try calling on behalf of the contract once set up

# How to run

- Create a file `.env` (you can use `.example.env` for reference)
- Input your private key and address into the `.env` file
- Ensure your wallet has HYPE on HyperEVM, HYPE on HyperCore and has [large blocks enabled](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/hyperevm/dual-block-architecture)
- Deploy the contract and call the function with `forge script script/SetUpApiWallet.s.sol:SetUpApiWalletScript --rpc-url https://rpc.hyperliquid.xyz/evm --broadcast`
- Copy the contract address that is logged (We need that later)
- Modify `api/main.py` to set the `CONTRACT` variable equal to the one that was just deployed
- Install dependencies with pip `hyperliquid-python-sdk` and `python-dotenv`
- Run with `python api/main.py`
- See that there is an error logged `Vault not registered` (this can be replicated with calling any function, `update_leverage` is just a conveneint one)
