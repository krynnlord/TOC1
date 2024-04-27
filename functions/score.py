from functions.classes import *
from functions.variables import *
import os
from rich.console import Console
from rich.theme import Theme

def display_score():
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)

    while True:
        os.system('cls')
        
        console.print("Name: " + hero[0].name)
        console.print("\nStats")
        for i in range(20): 
            console.print("-", end="")

        console.print("\nHit Points: " + str(hero[0].hp)+ "/" + str(hero[0].hp_max))
        console.print("Level: " + str(hero[0].level))
        console.print("Exp: " + str(hero[0].exp))
        console.print("Luck: " + str(hero[0].luck))
        console.print("Status: ", end="")
        if hero[0].stat == 1:
            console.print("Normal")
        elif hero[0].stat == 0:
            console.print("Dead")
        elif hero[0].stat == 2:
            console.print("Poisoned")     

        console.print("\nEquipment")
        for i in range(20): 
            console.print("-", end="")
        console.print("\nWeapon: " + hero[2].name)
        console.print("Armor: " + hero[1].name)
        ans = console.input("\n")

        break