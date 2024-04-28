from functions.gameFunctions import *
import functions.gameFunctions as l
from functions.variables import *
import  os
from rich.console import Console
from rich.theme import Theme

def blacksmith():
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/art/blacksmith.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        
        # Print Artwork
        console.print("[yellow]"+l.loadart(filetitle, data)+"[/yellow]\n")

        # Print Hero Information
        l.hero_status_bar(hero)
        
        # Print Choices
        console.print("([red]1[/red]) Buy Weapons")
        console.print("([red]2[/red]) Buy Armor")
        console.print("([red]3[/red]) Back")

        ans = console.input("\n[yellow]Selection> [/yellow]")

        # Run Choices
        if ans == '3':
            break
        
