#!/usr/bin/python3

from brownie import Token, accounts


def main():

    accounts.add('9fa44b230cadfd815b7d566708f3b2a2753ece818d0f94ef0caff79e75e68fab')

   

    return Token.deploy("SC", "TST", 18, 1e21, {'from': acct})
