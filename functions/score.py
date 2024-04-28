from functions.classes import *
import functions.gameFunctions as l
from functions.variables import *
import os
from rich.console import Console
from rich.theme import Theme

def display_score():
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)

    while True:
        os.system('cls')
        filetitle="asset/art/score.dat"
        data = ''
        console.print("[yellow]"+l.loadart(filetitle, data)+"[/yellow]\n")
        l.hero_status_bar(hero)
        console.print("Luck: " + str(hero[0].luck),)
        console.print("Status: ", end="")
        if hero[0].stat == 1:
            console.print("Normal")
        elif hero[0].stat == 0:
            console.print("Dead")
        elif hero[0].stat == 2:
            console.print("Poisoned")
        console.print("Damage Roll: " + hero[2].damage)
        console.print("Armor Class: " + str(hero[1].armorclass))
        ans = console.input("\n")

        break