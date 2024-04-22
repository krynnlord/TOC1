# Define Item Class
class Gear():

	def __init__(self, id, name, type, subtype, desc, attack, defense,value, qty):
		self.id = id
		self.name = name
		self.type = type
		self.type = subtype
		self.desc = desc
		self.attack = attack
		self.defense = defense
		self.value = value
		self.qty = qty
	
	def add(self,qty):
		self.qty += qty

	def remove(self,qty):
		self.qty -= qty


#########################
#  Gear  ################
#########################

# Weapons
small_sword = Gear(1, 'Small Sword','weapon', 'slashing', 'A small sword that does normal damage', 7, 0, 24, 1)
long_sword = Gear(2, 'Long Sword','weapon', 'slashing', 'A long sword that does significant damage', 15, 0, 80, 1)
mace = Gear(3, 'Mace','weapon','blunt', '...', 7, 0, 24, 1)
hammer = Gear(4, 'Hammer','weapon','blunt', '...', 12, 0, 75, 1)
Staff = Gear(5, 'Staff','weapon', 'blunt','...', 6, 0, 15, 1)
dagger = Gear(6, 'Dagger','weapon', 'slashing','...', 3, 0, 5, 1)
flail = Gear(7, 'Flail','weapon', 'blunt','...', 18, 0, 120, 1)

# Armor
cloth_armor = Gear(20, 'Cloth Armor','armor', 'light', 'A small robe that absorbs little damage', 0, 2, 24, 1)
leather_armor = Gear(21, 'Leather Armor','armor', 'medium', 'A small robe that absorbs little damage', 0, 2, 24, 1)
chain_armor = Gear(22, 'Chain Armor','armor', 'medium', 'A small robe that absorbs little damage', 0, 2, 24, 1)
plate_armor = Gear(23, 'Plate Armor','armor', 'heavy', 'A small robe that absorbs little damage', 0, 2, 24, 1)
