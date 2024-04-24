# Armor Class 
class armor:
    def __init__(self, name, type, cost, armorclass, description):
        self.name = name
        self.type = type
        self.cost = cost
        self.armorclass = armorclass
        self.description = description
         
# No Armor
tunic = armor("Hands", "blunt", 0, 1,"")

# Light
cloth_armor = armor("Cloth Armor", "Light", 50, 5, "")
leather_armor = armor("Leather Armor", "Light", 100, 11, "")

# Medium
chain_armor = armor("Chain Armor", "Medium", 500, 13, "")
scale_armor = armor("Scale Armor", "Medium", 600, 14, "")

# Heavy
splint_armor = armor("Splint Armor", "Heavy", 2000, 17, "")
plate_armor = armor("Plate Armor", "Heavy", 3000, 18, "")

# Hero obtained list
hero_armors = [tunic]