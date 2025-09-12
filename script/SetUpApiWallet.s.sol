// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import {Script, console} from "forge-std/Script.sol";
import {ApiWalletTest} from "../src/ApiWalletTest.sol";

contract SetUpApiWalletScript is Script {
    ApiWalletTest public apiWalletTest;

    function run() public {
        uint256 deployerPrivateKey_ = vm.envUint("PRIVATE_KEY");
        address deployerAddress_ = vm.addr(deployerPrivateKey_);
        vm.startBroadcast(deployerPrivateKey_);
        ApiWalletTest apiWalletTest_ = new ApiWalletTest();
        console.log("Contract deployed at:", address(apiWalletTest_));
        apiWalletTest_.addApiWallet(deployerAddress_, "");
        vm.stopBroadcast();
    }
}
