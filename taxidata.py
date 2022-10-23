from blondie.token.scripts.blockchain_interaction

class TaxiData:
	def __init__(self):
		#randomise starting values here
		self.id = -1
		self.x = -1
		self.y = -1
		self.price_min = -1
		self.base_price = -1
		self.available = -1
		self._isAlive = False
<<<<<<< Updated upstream

	def upload(self):

	# def setints(self,intsarray):
	# 	self.id = intsarray[0]
	# 	self.x = intsarray[1]
	# 	self.y = intsarray[2]
	# 	self.price_min = intsarray[3]
	# 	self.base_price = intsarray[4]

	# def setaddresses(address):
	# 	self.address = address
	#
	# def setbools(boolsarray):
	# 	if boolsarray[0]:
	# 		self.available = 1
	# 	else:
	# 		self.available = 0
	# 	self._isAlive = boolsarray[1]

	# def returnarray():
	# 	return [self.taxi_address,self.x,self.y,self.base_price,self.price_min,self.available]

=======
	
	def setints(intsarray):
		self.id = intsarray[0]
		self.x = intsarray[1]
		self.y = intsarray[2]
		self.price_min = intsarray[3]
		self.base_price = intsarray[4]
		
	def setaddresses(address):
		self.address = address
	
	def setbools(boolsarray):
		if boolsarray[0]:
			self.available = 1
		else:
			self.available = 0
		self._isAlive = boolsarray[1]
	
	def returnarray():
		return [self.id,self.x,self.y,self.base_price,self.price_min,self.available]

>>>>>>> Stashed changes
# alltaxiints = get_from_blockchain_ints()
# alltaxiaddresses = get_from_blockchain_addresses()
# alltaxibools = get_from_blockchain_bools()
# taxidatas = [TaxiData() for i in range(len(alltaxiints))]
# i = 0
# for td in taxidatas:
<<<<<<< Updated upstream
# 	td.setints(alltaxiints[i])
# 	td.setaddresses(alltaxiaddresses[i])
# 	td.setbools(alltaxibools[i])
# 	i+=1
#
=======
# 	td.setints(alltaxiints[i])x
# 	td.setaddresses(alltaxiaddresses[i])
# 	td.setbools(alltaxibools[i])
# 	i+=1
# 
>>>>>>> Stashed changes
# def listofalltaxidata():
# 	l = []
# 	for td in taxidatas:
# 		l.append(td.returnarray())
<<<<<<< Updated upstream
# 	return l
=======
# 	return l
>>>>>>> Stashed changes
