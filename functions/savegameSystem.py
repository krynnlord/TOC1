import json

# Savegame_hero Function
def savegame_hero(hero):
    with open('hero.dat','w') as file:
        json.dump(hero,file)

# Savegame_inventory Function
def savegame_inventory(inventory):        
    with open('inventory.dat','w') as file:
        json.dump(inventory,file)    
    
# Loadgame_hero Function
def loadgame_hero(data):
    with open('hero.dat','r') as file:
        data = json.load(file)
        return data
    
# Loadgame_inventory Function
def loadgame_inventory(data):
    with open('inventory.dat','r') as file:
        data = json.load(file)
        return data

# Debug Print Stats
def print_stats(hero, inventory):
    print(hero)
    print(inventory) 