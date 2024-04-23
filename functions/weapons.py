# Weapons Class 
class weapon:
    def __init__(self, name, type, cost, damage, description):
        self.name = name
        self.type = type
        self.cost = cost
        self.damage = damage
        self.description = description
         
# Blunt
club = weapon("Club", "blunt", 10, "1d4", "")
greatclub = weapon("Greatclub", "blunt", 20, "1d8", "")
lighthammer = weapon("Light Hammer", "blunt", 20, "1d4", "")
mace = weapon("Mace", "blunt", 500, "1d6", "")

# Slashing
dagger = weapon("Dagger", "slashing", 200, "1d4", "")
handaxe = weapon("Handaxe", "slashing", 500, "1d6", "")

# Hero obtained list
hero_weapons = [dagger, handaxe, club, greatclub, lighthammer]
