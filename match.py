import pandas as pd
import taxidata
from blondie.token.scripts.blockchain_interaction import *
import numpy as np
from random import randint

class Match:
    
    def __init__(self,fx,fy,tx,ty,taxis):
        print(fx,fy,tx,ty)
        self.passenger_loc = (int(fx),int(fy))
        self.passenger_dest = (int(tx),int(ty))
        self.cars_data = np.squeeze(np.transpose(list(taxis)), 1)
        print(self.cars_data)
        self.num_cars = len(self.cars_data)
        self.cars = pd.DataFrame(data=self.cars_data,
                                 index=['car' + str(i + 1) for i in range(self.num_cars)],
                                 columns=['Id', 'X location', 'Y location', 'Base Price', 'Price/min']
                                )

    def available(self):
        '''Filters out unavailable cars.'''
        return self.cars.loc[self.cars.Available==1]

    def match(self):
#         '''
#         Returns the (taxicab) distance of the passenger from each car in cars.
#         passenger = tuple representing the passenger location
#         cars = dataframe
# 
#         Distance metric can be altered to factor in road network type, driver costs.
#         '''
# 
# 
#         if len(self.cars)==0:
#             return None
#         else:
#             # change_in_loc = self.cars.loc[:,['X location','Y location']] - self.passenger_loc
#             # distances = pd.DataFrame(
#             #     data=[self.cars.Id.values,change_in_loc.abs().sum(1)],
#             #     index=self.cars.index,
#             #     columns=['Id','Distance']
#             # )
#             # match = distances.loc[distances.Distance==distances.Distance.min()]
#             # if len(match)>1: # If there are multiple matches, we select one randomly.
#             #     match = match.sample(n=1)
#             #     pair(match.values[0][0], self.passenger_loc[0], self.passenger_loc[1], self.passenger_dest[0], self.passenger_dest[1])
#             # else:
#             #     pair(match.values[0][0], self.passenger_loc[0], self.passenger_loc[1], self.passenger_dest[0], self.passenger_dest[1])
#             match = match.sample(n=1)
#             pair(match.values[0][0], self.passenger_loc[0], self.passenger_loc[1], self.passenger_dest[0], self.passenger_dest[1])
#         car_id = match.index[0]
#         time_until_pickup = match.Distance[0]
#         journey_time = 4
#         
        slice = self.cars_data[randint(0, len(self.cars))]
        pair(slice[0],slice[1],slice[2],slice[3],slice[4])
        
        return slice[0], 'Bob', 1, 2
