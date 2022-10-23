import numpy as np

def init_locations():
    '''
    Randomly generates starting coordinates for a car.
    '''
    return np.random.randint(0,high=5,size=2)
