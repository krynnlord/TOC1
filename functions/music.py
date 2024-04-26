import functions.gameFunctions as l
import os
from rich.console import Console
from rich.theme import Theme

def music():
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/music.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        console.print("[cyan]"+l.loadart(filetitle, data)+"[/cyan]\n\n")
  
        # Print Choices
        console.print("[yellow]1[/yellow]) Moonlight Sonata    [yellow]6[/yellow]) Moonlight Sonata")
        console.print("[yellow]2[/yellow]) Moonlight Sonata    [yellow]7[/yellow]) Moonlight Sonata")
        console.print("[yellow]3[/yellow]) Moonlight Sonata    [yellow]8[/yellow]) Moonlight Sonata")
        console.print("[yellow]4[/yellow]) Moonlight Sonata    [yellow]9[/yellow]) Moonlight Sonata")
        console.print("[yellow]5[/yellow]) Moonlight Sonata   [yellow]10[/yellow]) Moonlight Sonata")
        console.print("\n[yellow]11[/yellow]) Back")
        ans = console.input("\n[yellow]Selection> [/yellow]")

        if ans == '1':
            l.play_midi("asset/music/01.mid", 1)
        if ans == '2':
            l.play_midi("asset/music/02.mid", 1)
        if ans == '3':
            l.play_midi("asset/music/03.mid", .5)
        if ans == '4':
            l.play_midi("asset/music/04.mid", 1)
        if ans == '5':
            l.play_midi("asset/music/05.mid", 1)            
        if ans == '6':
            l.play_midi("asset/music/06.mid", 1)
        if ans == '7':
            l.play_midi("asset/music/07.mid", 1)
        if ans == '8':
            l.play_midi("asset/music/08.mid", 1)
        if ans == '9':
            l.play_midi("asset/music/09.mid", 1)
        if ans == '10':
            l.play_midi("asset/music/10.mid", 1)
        if ans == '11':
            return
