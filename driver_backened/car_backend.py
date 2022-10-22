import pandas as pd
from brookie.scripts.blockchain_interaction import *

# This will eventually be the taxi front end pressing a button to say available
taxi_info = pd.Series(data=[1,2,3,4,1],)

# add taxi availabile to blockchain dataset (including updates of price etc)
def set_availability(available):
	add_taxi(taxi_info)
# check for broadcast of pair that includes your own address

# check your own wallet to see if payment has been made

# once pair is received, send to blockchain that payment is received, and set availabile = 0

# check for broadcast of end journey, then set available = 1
