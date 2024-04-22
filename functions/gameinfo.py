import os
import functions.gameFunctions as l
from rich.console import Console
from rich.theme import Theme


def gameinfo():
    
    os.system("cls")
    data = ''
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme)
    filetitle = 'asset/gameinfo.dat'
    console.print("[yellow]"+l.loadart(filetitle, data)+"[/yellow]\n\n")
    
    console.print("[yellow]     Game:[/yellow] "+l.GameDescInfo["GameTitle"] + ' - ' + l.GameDescInfo["GameSubtitle"])
    console.print("[yellow]Copyright:[/yellow] "+l.GameDescInfo["Copyright"])
    console.print("[yellow]   Author:[/yellow] "+str(l.GameDescInfo["Author"]))
    console.print("[yellow]  Version:[/yellow] "+str(l.GameDescInfo["GameVersion"]))

    console.input('\n[yellow]Press any key to return...[/yellow]')