// SPDX-License-Identifier: MIT

// Basic balance file given by Solidity

pragma solidity ^0.8.0;

contract contractBalance {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }
}