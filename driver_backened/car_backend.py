import pandas as pd
from blondie.token.scripts.blockchain_interaction import *
from taxidata import TaxiData
import multiprocessing as mp
from random import randint

class Taxi:
	def __init__(self, base_price, min_price):
		self.x = randint(0,4)
		self.y = randint(0,4)
		self.base_price = base_price
		self.min_price = min_price

	def upload(self):
		self.id = add_taxi(self.x,self.y,self.base_price,self.min_price)


def taximain(base_price, min_price, num_cars):
	taxi_datas = [Taxi(base_price, min_price) for i in range(int(num_cars))]
	[x.upload() for x in taxi_datas]
	ids = [x.id for x in taxi_datas]
	print(type(ids[0]))
	
	def taxi_running(id):
		while True:
			__, __, (x,y) = search_and_find_pair(id)
			taxi_during_route(id, x, y)

	with mp.Pool(int(num_cars)) as p:
		p.map(taxi_running,ids)
