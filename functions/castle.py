from functions.gameFunctions import *
import functions.gameFunctions as l
from functions.variables import *
import  os
from rich.console import Console
from rich.theme import Theme

def castle():
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/art/castle.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        
        # Print Artwork
        console.print("[yellow]"+l.loadart(filetitle, data)+"[/yellow]\n")

        # Print Hero Information
        l.hero_status_bar(hero)
        
        # Print Choices
        console.print("([red]1[/red]) Speak with King")
        console.print("([red]2[/red]) Back")

        ans = console.input("\n[yellow]Selection> [/yellow]")

        # Run Choices
        if ans == '1':
            hero[0].level = '2'
            hero[0].exp = 200
            hero[1] = chain_armor
            hero[2] = shortsword
        if ans == '2':
            break
        
