import pandas as pd
from brookie.scripts.blockchain_interaction import *
from taxidata import TaxiData
import multiprocessing as mp


taxi_datas = [TaxiData for i in range(mp.cpu_count())]

# check for broadcast of pair that includes your own address
def is_pair():
    '''
    reads pair from the blockchain, checks whether the pair includes your own address.
    '''
	search_and_find_pair(my_address)
    # if pair.loc['Address']==my_address:
        # send to blockchain that payment is made
        # edit taxidata so that available = 0


# check your own wallet to see if payment has been made

# once pair is received, send to blockchain that payment is received, and set availabile = 0

# check for broadcast of end journey, then set available = 1
