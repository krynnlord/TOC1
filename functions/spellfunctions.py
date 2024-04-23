import os
from rich.console import Console
from rich.theme import Theme
from functions.spellVariables import *

custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
console = Console(theme=custom_theme)

def spellcast(hero_spells):

    for i in hero_spells:
        if i.ready == 1 and i.qty > 0:              
            console.print("[white]" + i.name + "[/white]("+str(i.qty) + ") ", end="")   

    ans2 = console.input("\nCast which spell? ")
    
    if ans2.lower() in ["fir", "fireball"] and fireball.qty > 0:
        console.input("You cast [red]Fireball[/red]")
        fireball.qty-= 1

    elif ans2.lower() in ["hea", "heal"] and heal.qty > 0:
        console.input("You cast [red]Heal[/red]")
        heal.qty -= 1        
    
    else:
        console.input("That is not a valid spell.")   