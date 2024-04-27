# The Oblivion Cycle - Chapter I: The Shimmering Gate
# (C)opyright 2024 RLM Productions

import functions.gameFunctions as l
import sqlite3, os
from rich.console import Console
from rich.theme import Theme

# Temp Skip Here
# l.adventuremenu()

# Read Game Options from database
con = sqlite3.connect('data.db')
cur = con.cursor()
result_music = cur.execute("select value from options where id = 1").fetchone() # 0 music is Off 1 is on
result_musictrack = cur.execute("select value from options where id = 3").fetchone() # music choice
result_title = cur.execute("select value from options where id = 2").fetchone() # 0 is show title 1 is skip

if result_music[0] == 1: # Check for Music
    music_selected = f'{result_musictrack[0]:02d}' # Convert to 2 digits if 1
    musictrack = 'asset/music/'+str(music_selected)+'.mid'
    l.play_midi(musictrack,1) # play Music 

if result_title[0] == 1: # Check for Intro
    l.intro()

### Main Menu ###
while True:
    os.system('cls')
    ans = ''
    filetitle = 'asset/title.dat'
    data = ''
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)
    console.print("[red]"+l.loadart(filetitle, data)+"[/red]")
    console.print("                          Chapter I: The Shimmering Gate")
    console.print('')

    # Print Choices
    console.print("([red]1[/red]) Play Game")
    console.print("([red]2[/red]) New Game")
    console.print("([red]3[/red]) Game Options")
    console.print("([red]4[/red]) Quit Game")
    ans = console.input("\n[yellow]Selection> [/yellow]")

    # Run Choices
    if ans == '2':
        l.createhero()
    elif ans == '1':
        l.adventuremenu()
    elif ans == '3':
        l.gameoptions()
    elif ans == '4':
        break
    elif ans == 'b': # Test out new battle simulation
        l.battle_seq()
    elif ans == 'B': # Test out retro battle simulation
        l.r_battle_seq()


### MAIN CODE ###


### EXIT CODE ###
con.close()
os.system('cls')