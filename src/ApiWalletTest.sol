// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import {CoreWriterLib} from "@hyper-evm-lib/src/CoreWriterLib.sol";

contract ApiWalletTest {
    function addApiWallet(address wallet, string memory name) public {
        CoreWriterLib.addApiWallet(wallet, name);
    }
}
