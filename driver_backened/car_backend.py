import pandas as pd
from brookie.scripts.blockchain_interaction import *

# check for broadcast of pair that includes your own address
my_address = 'my_wallet_address'

def is_pair():
    '''
    reads pair from the blockchain, checks whether the pair includes your own address.
    '''
    pair = get_pair_info()
    if pair.loc['Address']==my_address:
        # send to blockchain that payment is made
        # edit taxidata so that available = 0
    else:
        # ?

# check your own wallet to see if payment has been made

# once pair is received, send to blockchain that payment is received, and set availabile = 0

# check for broadcast of end journey, then set available = 1
