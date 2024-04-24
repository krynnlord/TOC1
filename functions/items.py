# Define Item Class
class item():

	def __init__(self, name, type,  value, qty, desc):
		self.name = name
		self.type = type
		self.value = value
		self.qty = qty
		self.desc = desc
	
	def add(self,qty):
		self.qty += qty

	def remove(self,qty):
		self.qty -= qty


#########################
# Base Items ############
#########################

# Items
potion = item("Potion of Healing", "potion", 500, 1, "") # 2d4 + 2 of healing, takes an action
