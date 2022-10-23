import pandas as pd
from brookie.scripts.blockchain_interaction import *
from taxidata import TaxiData
import multiprocessing as mp
from random import randint

class Taxi:
	def __init__(self, base_price, min_price):
		self.x = randint(-5,5)
		self.y = randint(-5,5)
		self.base_price = base_price
		self.min_price = min_price

	def upload(self):
		self.id = add_taxi(self.x,self.y,self.base_price,self.min_price)


def taximain(base_price, min_price, num_cars):
	taxi_datas = [Taxi(base_price, min_price) for i in range(num_cars)]
	[x.upload() for x in taxi_datas]

	def taxi_running(taxi):
		while True:
			__, __, (x,y) = search_and_find_pair(taxi.id)

			taxi_during_route(taxiid, x, y)

	with mp.Pool(num_cars) as p:
		p.map(taxi_running,taxi_datas)
