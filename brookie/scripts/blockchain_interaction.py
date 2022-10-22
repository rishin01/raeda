
from brownie import *


# Calls the smart contract
SC = Contract(<number>) # do we need abi here too? ABI is just a 'list' thing of functions and events

# Accesses passenger wallet
accounts.add('9fa44b230cadfd815b7d566708f3b2a2753ece818d0f94ef0caff79e75e68fab')

#access account via accounts[0]

def readTaxi():
	'''
	Gets all taxi info from the blockchain.
	'''
    event = SC.Available()
    #this might not work
    return event


def add_taxi(taxi_info):
	'''
	adds input to blockchain taxi info
	'''
    SC.add_taxi(*taxi_info)

def pair(car_id):
	'''
	sends the pairing (found by match.py) to the blockchain
	'''
    receipt = SC.pair(car_id)
    paired = SC.Paired() #this might not work
    check_my_wallet = receipt.internal_transfers[0]['from']

def passenger_update_taxi_location(taxiid, x, y):
	'''
	not relevent yet
	'''
    receipt = SC.passenger_update_taxi_location(taxiid, x, y)





#add_taxi, pair, passenger_update_taxi_location , taxi_owner_update_details , exit_taxi
