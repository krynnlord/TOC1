# Define Item Class
class Item():

	def __init__(self, id, name, type, desc, value, qty):
		self.id = id
		self.name = name
		self.type = type
		self.desc = desc
		self.value = value
		self.qty = qty
	
	def add(self,qty):
		self.qty += qty

	def remove(self,qty):
		self.qty -= qty


#########################
# Base Items ############
#########################

# Items

