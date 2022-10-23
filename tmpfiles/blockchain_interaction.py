
from brownie import *

print(network.is_connected())
network.connect('matic_mumbai')
print(network.is_connected())

accounts.add('9fa44b230cadfd815b7d566708f3b2a2753ece818d0f94ef0caff79e75e68fab')
SC = Contract('0xC01C79D1fD24b920058F063c37817c96F028aCb6', owner = accounts[0]) # do we need abi here too? ABI is just a 'list' thing of functions and events




#access account via accounts[0]

def find_taxis():
    n = SC.check_number_available()

    ids = []
    xs = []
    ys = []
    base_prices = []
    price_mins = []
    for i in range(n):
        ids.append(SC.check_available_taxi_ids(i))
        xs.append(SC.check_available_taxi_x(i))
        ys.append(SC.check_available_taxi_y(i))
        base_prices.append(SC.check_available_taxi_base_price(i))
        price_mins.append(SC.check_available_taxi_price_min(i))
    return ids, xs, ys, base_prices, price_mins


def add_taxi(x,y,base_price, price_min):
	taxi_id = SC.add_taxi(x,y,base_price,price_min).return_value
	return taxi_id

def search_and_find_pair(taxi_id):
	while True:
		matched_bool = SC.check_for_pair(taxi_id)
		if matched_bool:
			break
	passenger_address = SC.retrieve_passenger_address(taxi_id)
	x_current = SC.retriever_x_current(taxi_id)
	y_current = SC.retriever_y_current(taxi_id)
	x_dest = SC.retriever_x_dest(taxi_id)
	y_dest = SC.retriever_y_dest(taxi_id)


	return passenger_address, (x_current, y_current), (x_dest, y_dest)

def taxi_during_route(taxiid,x,y):
	while True:
		if SC.taxi_end_journey(taxiid, x, y):
			break

def passenger_end_journey(taxiid):
	SC.passenger_end_journey(taxiid)

	#Makes taxi available again


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
