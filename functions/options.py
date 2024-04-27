import functions.gameFunctions as l
import sqlite3, os
from rich.console import Console
from rich.theme import Theme

def gameoptions():
    
    while True:
        os.system('cls')
        ans = ''
        filetitle = 'asset/art/options.dat'
        data = ''
        custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
        console = Console(theme=custom_theme, highlight=None)
        console.print("[yellow]"+l.loadart(filetitle, data)+"[/yellow]\n\n")

        # Read Game Options from database
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        result_music = cur.execute("select value from options where id = 1").fetchone() 
        result_title = cur.execute("select value from options where id = 2").fetchone()
        result_battle = cur.execute("select value from options where id = 4").fetchone() 
        

        # Print Choices
        if result_title[0] == 0:
            console.print("([red]1[/red]) Show Intro (Currently: [red]Off[/red])")
        else:
            console.print("([red]1[/red]) Show Intro (Currently: [green]On[/green])")

        if result_music[0] == 1:            
            console.print("([red]2[/red]) Play Music (Currently: [green]On[/green])")
        else:    
            console.print("([red]2[/red]) Play Music (Currently: [red]Off[/red])")
        
        if result_battle[0] == 1:            
            console.print("([red]3[/red]) Modern Battle System (Currently: [green]On[/green])")
        else:    
            console.print("([red]3[/red]) Modern Battle System (Currently: [red]Off[/red])")
        console.print("([red]4[/red]) Game Information")
        console.print("([red]5[/red]) Music Player")
        console.print("([red]6[/red]) Return")

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
                l.music_toggle()
            else:
                cur.execute("update options set value = 1 where id = 1")
                con.commit()
                result_musictrack = cur.execute("select value from options where id = 3").fetchone()
                music_selected = f'{result_musictrack[0]:02d}' # Convert to 2 digits if 1
                musictrack = 'asset/music/'+str(music_selected)+'.ogg'
                l.play_music(musictrack)
        
        elif ans == '3': # Toggle Battle Version
            
            if result_battle[0] == 1:
                cur.execute("update options set value = 0 where id = 4")
                con.commit()
            else:
                cur.execute("update options set value = 1 where id = 4")
                con.commit()                
        
        elif ans == '4':
            l.gameinfo()
        
        elif ans == '5':
            l.music()
        
        elif ans == '6':
            break
    