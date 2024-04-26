import functions.gameFunctions as l
import sqlite3, os
from rich.console import Console
from rich.theme import Theme

def gameoptions():
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/options.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        console.print("[yellow]"+l.loadart(filetitle, data)+"[/yellow]\n\n")

        # Read Game Options from database
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        result_music = cur.execute("select value from options where id = 1").fetchone() # 0 music is Off 1 is on
        result_title = cur.execute("select value from options where id = 2").fetchone() # 0 is show title 1 is skip
        

        # Print Choices
        if result_title[0] == 1:
            console.print("([red]1[/red]) Show Intro (Currently: Off)")
        else:
            console.print("([red]1[/red]) Show Intro (Currently: On)")

        if result_music[0] == 1:            
            console.print("([red]2[/red]) Play Music (Currently: On)")
        else:    
            console.print("([red]2[/red]) Play Music (Currently: Off)")

        console.print("([red]3[/red]) Game Information")
        console.print("([red]4[/red]) Music Player")
        console.print("([red]5[/red]) Return")

        ans = console.input("\n[yellow]Selection> [/yellow]")

        # Run Choices
        if ans == '1': # Toggle Intro Logic
            
            if result_title[0] == 1:
                cur.execute("update options set value = 0 where id = 2")
                con.commit()
            else:
                cur.execute("update options set value = 1 where id = 2")
                con.commit()

        elif ans == '2': # Toggle Music Logic
            if result_music[0] == 1:
                cur.execute("update options set value = 0 where id = 1")
                con.commit()
                l.midi_toggle()
                # l.music_toggle()
            else:
                cur.execute("update options set value = 1 where id = 1")
                con.commit()
                l.play_midi('asset/music/01.mid',1)
                # l.play_music('asset/title.mp3',0.3)

        elif ans == '3':
            l.gameinfo()
        
        elif ans == '4':
            l.music()
        
        elif ans == '5':
            break
    
