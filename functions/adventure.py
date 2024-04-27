from functions.gameFunctions import *
import functions.gameFunctions as l
from functions.variables import *
import  os
from rich.console import Console
from rich.theme import Theme

def adventuremenu():
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/art/village.dat'
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
            console.print("-", end="")

        console.print("\n")
        
        # Print Choices
        console.print("([red]1[/red]) The Circle of Stones")
        console.print("([red]2[/red]) The Castle")
        console.print("([red]3[/red]) The Temple")
        console.print("([red]4[/red]) The Blacksmith")
        console.print("([red]5[/red]) The Provisioner")
        console.print("([red]6[/red]) The Inn")
        console.print("([red]7[/red]) Back to Main Menu")

        ans = console.input("\n[yellow]Selection> [/yellow]")

        # Run Choices
        if ans == '1':
            l.stones()
        elif ans == '2':
            l.castle()
        elif ans == '3':
            l.temple()
        elif ans == '4':
            l.blacksmith()
        elif ans == '5':
            l.provisioner()          
        elif ans == '6':
            l.inn()
        elif ans == 's' or ans == 'S':
            l.display_score()    
        elif ans == '7':
            break
        
