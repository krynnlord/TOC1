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
        console.print("[yellow]1[/yellow]) Elven Ruins         [yellow]7[/yellow]) The Iron Wall")
        console.print("[yellow]2[/yellow]) To Oblivion         [yellow]8[/yellow]) Lullaby")
        console.print("[yellow]3[/yellow]) Mysterious Portal   [yellow]9[/yellow]) Spiraling Descent")
        console.print("[yellow]4[/yellow]) Cryptic Walls      [yellow]10[/yellow]) Distant Stars")
        console.print("[yellow]5[/yellow]) Bard's Story       [yellow]11[/yellow]) Judgement")
        console.print("[yellow]6[/yellow]) Shimmering Lights  [yellow]12[/yellow]) Ascendancy")
        console.print("\n[yellow]0[/yellow]) Back")
        ans = console.input("\n[yellow]Selection> [/yellow]")

        con = sqlite3.connect('data.db')
        cur = con.cursor()


        if ans == '1':
            l.play_music("asset/music/01.ogg")
            cur.execute("update options set value = 1 where id = 3")
            con.commit()
        if ans == '2':
            l.play_music("asset/music/02.ogg")
            cur.execute("update options set value = 2 where id = 3")
            con.commit()
        if ans == '3':
            l.play_music("asset/music/03.ogg")
            cur.execute("update options set value = 3 where id = 3")
            con.commit()
        if ans == '4':
            l.play_music("asset/music/04.ogg")
            cur.execute("update options set value = 4 where id = 3")
            con.commit()
        if ans == '5':
            l.play_music("asset/music/05.ogg")
            cur.execute("update options set value = 5 where id = 3")
            con.commit()            
        if ans == '6':
            l.play_music("asset/music/06.ogg")
            cur.execute("update options set value = 6 where id = 3")
            con.commit()
        if ans == '7':
            l.play_music("asset/music/07.ogg")
            cur.execute("update options set value = 7 where id = 3")
            con.commit()
        if ans == '8':
            l.play_music("asset/music/08.ogg")
            cur.execute("update options set value = 8 where id = 3")
            con.commit()
        if ans == '9':
            l.play_music("asset/music/09.ogg")
            cur.execute("update options set value = 9 where id = 3")
            con.commit()
        if ans == '10':
            l.play_music("asset/music/10.ogg")
            cur.execute("update options set value = 10 where id = 3")
            con.commit()
        if ans == '11':
            l.play_music("asset/music/11.ogg", .3)
            cur.execute("update options set value = 11 where id = 3")
            con.commit()
        if ans == '12':
            l.play_music("asset/music/12.ogg", .3)
            cur.execute("update options set value = 12 where id = 3")
            con.commit()            

        if ans == '0':
            return
