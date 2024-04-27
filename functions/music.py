import functions.gameFunctions as l
import os, sqlite3
from rich.console import Console
from rich.theme import Theme

def music():
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/art/music.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        console.print("[cyan]"+l.loadart(filetitle, data)+"[/cyan]\n\n")
  
        # Print Choices
        console.print("[yellow]1[/yellow]) Moonlight Sonata    [yellow]6[/yellow]) Totentanz")
        console.print("[yellow]2[/yellow]) Toccata & Fugue     [yellow]7[/yellow]) Funeral March 2")
        console.print("[yellow]3[/yellow]) Funeral March       [yellow]8[/yellow]) Bald Mountain")
        console.print("[yellow]4[/yellow]) Mountain King       [yellow]9[/yellow]) Spirit Lulliby")
        console.print("[yellow]5[/yellow]) Danse Macabre      [yellow]10[/yellow]) Hungarian Dance")
        console.print("\n[yellow]11[/yellow]) Back")
        ans = console.input("\n[yellow]Selection> [/yellow]")

        con = sqlite3.connect('data.db')
        cur = con.cursor()


        if ans == '1':
            l.play_midi("asset/music/01.mid", 1)
            cur.execute("update options set value = 1 where id = 3")
            con.commit()
        if ans == '2':
            l.play_midi("asset/music/02.mid", 1)
            cur.execute("update options set value = 2 where id = 3")
            con.commit()
        if ans == '3':
            l.play_midi("asset/music/03.mid", 1)
            cur.execute("update options set value = 3 where id = 3")
            con.commit()
        if ans == '4':
            l.play_midi("asset/music/04.mid", 13)
            cur.execute("update options set value = 4 where id = 3")
            con.commit()
        if ans == '5':
            l.play_midi("asset/music/05.mid", 1)
            cur.execute("update options set value = 5 where id = 3")
            con.commit()            
        if ans == '6':
            l.play_midi("asset/music/06.mid", 1)
            cur.execute("update options set value = 6 where id = 3")
            con.commit()
        if ans == '7':
            l.play_midi("asset/music/07.mid", 1)
            cur.execute("update options set value = 7 where id = 3")
            con.commit()
        if ans == '8':
            l.play_midi("asset/music/08.mid", 1)
            cur.execute("update options set value = 8 where id = 3")
            con.commit()
        if ans == '9':
            l.play_midi("asset/music/09.mid", 1)
            cur.execute("update options set value = 9 where id = 3")
            con.commit()
        if ans == '10':
            l.play_midi("asset/music/10.mid", 1)
            cur.execute("update options set value = 10 where id = 3")
            con.commit()
        if ans == '11':
            return
