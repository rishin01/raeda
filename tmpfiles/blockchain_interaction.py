
from brownie import *

print(network.is_connected())
network.connect('matic_mumbai')
print(network.is_connected())

accounts.add('9fa44b230cadfd815b7d566708f3b2a2753ece818d0f94ef0caff79e75e68fab')
SC = Contract('0x96aEd0aebDAc2C81643AA3bf18E216f75908399c', owner = accounts[0]) # do we need abi here too? ABI is just a 'list' thing of functions and events




#access account via accounts[0]

def find_taxis():
    n = SC.check_number_available()

    addresses = []
    xs = []
    ys = []
    base_prices = []
    price_mins = []
    for i in range(n):
        addresses.append(SC.check_available_taxi_addresses(i))
        xs.append(SC.check_available_taxi_x(i))
        ys.append(SC.check_available_taxi_y(i))
        base_prices.append(SC.check_available_taxi_base_price(i))
        price_mins.append(SC.check_available_taxi_price_min(i))
    return addresses, xs, ys, base_prices, price_mins


def add_taxi(x,y,base_price, price_min):
    SC.add_taxi(x,y,base_price,price_min)
#
# def pair(car_id):
#     receipt = SC.pair(car_id)
#     paired = SC.Paired() #this might not work
#     check_my_wallet = receipt.internal_transfers[0]['from']
#
# def passenger_update_taxi_location(taxiid, x, y):
#     receipt = SC.passenger_update_taxi_location(taxiid, x, y)
#
#
# def main():
#     accounts.add('9fa44b230cadfd815b7d566708f3b2a2753ece818d0f94ef0caff79e75e68fab')
#     SC = Contract('0x96aEd0aebDAc2C81643AA3bf18E216f75908399c', owner = accounts[0]) # do we need abi here too? ABI is just a 'list' thing of functions and events
#
#     SC.add_taxi(1,2,3,4)
#     SC.add_taxi(1,5,3,6)
#     SC.add_taxi(9,5,2,3)
#
#     n = SC.check_number_available()
#
#     addresses = []
#     xs = []
#     ys = []
#     base_prices = []
#     price_mins = []
#     for i in range(n):
#         addresses.append(SC.check_available_taxi_addresses(i))
#         xs.append(SC.check_available_taxi_x(i))
#         ys.append(SC.check_available_taxi_y(i))
#         base_prices.append(SC.check_available_taxi_base_price(i))
#         price_mins.append(SC.check_available_taxi_price_min(i))
#
#
#
#
#
#


#add_taxi, pair, passenger_update_taxi_location , taxi_owner_update_details , exit_taxi
