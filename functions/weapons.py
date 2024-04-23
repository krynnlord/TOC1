# Weapons Class 
class weapon:
    def __init__(self, name, type, cost, dicecount, dicevalue):
        self.name = name
        self.type = type
        self.cost = cost
        self.dicecount = dicecount
        self.dicevalue = dicevalue
        
# Blunt
club = weapon("Club", "blunt", 10, 1, 4,"")
greatclub = weapon("Greatclub", "blunt", 20, 1, 8,"")
lighthammer = weapon("Light Hammer", "blunt", 20, 1, 4,"")
mace = weapon("Mace", "blunt", 500, 1, 6,"")

# Slashing
dagger = weapon("Dagger", "slashing", 200, 1, 4,"")
handaxe = weapon("Handaxe", "slashing", 500, 1, 6,"")

# Hero obtained list
hero_weapons = [dagger, handaxe, club, greatclub, lighthammer]
