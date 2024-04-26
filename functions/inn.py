from functions.gameFunctions import *
from functions.variables import *
import  os
from rich.console import Console
from rich.theme import Theme

def inn():
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/inn.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        
        # Print Artwork
        console.print("[yellow]"+l.loadart(filetitle, data)+"[/yellow]\n")

        # Print Hero Information
        for i in range(80):
            console.print ("-", end="")
        console.print("\n[white]"+hero[0].name + "   Level: " + str(hero[0].level) + "   Exp: " + str(hero[0].exp)+"[/white]", end="   ")
        console.print("[white]Armor: " + hero[1].name + "   Weapon: " + hero[2].name+"[/white]")
        for i in range(80):
            console.print ("-", end="")
        console.print("\n")
        
        # Print Choices
        console.print("([red]1[/red]) Rest")
        console.print("([red]2[/red]) Open Wardrobe")
        console.print("([red]3[/red]) Back")

        ans = console.input("\n[yellow]Selection> [/yellow]")

        # Run Choices
        if ans == '3':
            break
        
