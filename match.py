import pandas as pd
import taxidata
from blondie.token.scripts.blockchain_interaction import *
import numpy as np

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
        '''
#         Returns the (taxicab) distance of the passenger from each car in cars.
#         passenger = tuple representing the passenger location
#         cars = dataframe
# 
#         Distance metric can be altered to factor in road network type, driver costs.
#         '''
# 
#           
        match = self.cars.iloc[-1,:]
#         if len(self.cars)==0:
#             return None
#         else:
#             change_in_loc = self.cars.loc[:,['X location','Y location']] - self.passenger_loc
#             distances = pd.DataFrame(
#                 data=[self.cars.Id.values,change_in_loc.abs().sum(1)],
#                 index=self.cars.index,
#                 columns=['Id','Distance']
#             )
#             match = distances.loc[distances.Distance==distances.Distance.min()]
#             if len(match)>1: # If there are multiple matches, we select one randomly.
#                 match = match.sample(n=1)
        pair(match.loc['Id'], self.passenger_loc[0], self.passenger_loc[1], self.passenger_dest[0], self.passenger_dest[1])
#             else:
#                 pair(match.loc['Id'], self.passenger_loc[0], self.passenger_loc[1], self.passenger_dest[0], self.passenger_dest[1])
#         car_name = match.index[0]
#         time_until_pickup = match.Distance
#         journey_time = sum(self.passenger_dest - self.passenger_loc)
#         return match.loc['Id'],  car_name, time_until_pickup, journey_time
    
