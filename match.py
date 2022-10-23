import pandas as pd
from brookie.scripts.blockchain_interaction import *

class Match:
    
    def __init__():
        self.passenger_loc = (int(data['from'][1]),int(data['from'][3]))
        self.passenger_dest = (int(data['to'][1]),int(data['to'][3]))
        self.cars = pd.DataFrame(data=[[0,1,2,1,1],[2,4,1,2,0],[1,0,1,2,1]],
                                 index=['car1','car2','car3'],
                                 columns=['X location', 'Y location', 'Base Price', 'Price/min', 'Available']
                                )
        # cars = readTaxi()
        
    def available(self):
        '''Filters out unavailable cars.'''
        return self.cars.loc[self.cars.Available==1]

    def match(self):
        '''
        Returns the (taxicab) distance of the passenger from each car in cars.
        passenger = tuple representing the passenger location
        cars = dataframe

        Distance metric can be altered to factor in road network type, driver costs.
        '''
        self.cars = available(self.cars)

        if len(self.cars)==0:
            return None
        else:
            change_in_loc = self.cars.loc[:,['X location','Y location']] - self.passenger_loc
            distances = pd.DataFrame(data=change_in_loc.abs().sum(1),
                                     index=self.cars.index,
                                     columns=['Distance']
                                    )
            match = distances.loc[distances.Distance==distances.Distance.min()]
            if len(match)>1: # If there are multiple matches, we select one randomly.
                match = match.sample(n=1)
                pair(match.index[0])
            else:
                pair(match.index[0])
        return
