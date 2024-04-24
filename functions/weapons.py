# Weapons Class 
class weapon:
    def __init__(self, name, type, cost, damage, description):
        self.name = name
        self.type = type
        self.cost = cost
        self.damage = damage
        self.description = description
         
# No Weapon
hands = weapon("Hands", "blunt", 0, "1d2","")

# Blunt
club = weapon("Club", "blunt", 200, "1d4", "")
mace = weapon("Mace", "blunt", 500, "1d6", "")
lighthammer = weapon("Light Hammer", "blunt", 1000, "1d8", "")
warhammer = weapon("warhammer", "blunt", 1000, "1d10", "")
maul = weapon("Maul", "blunt", 5000, "2d6", "")

# Slashing
dagger = weapon("Dagger", "slashing", 200, "1d4", "")
handaxe = weapon("Handaxe", "slashing", 500, "1d6", "")
shortsword = weapon("Short Sword", "slashing", 1000, "1d8", "")
longsword = weapon("Long Sword", "slashing", 1500, "1d10", "")
greatsword = weapon("Great Sword", "slashing", 5000, "2d6", "")

# Hero obtained list
hero_weapons = [hands]