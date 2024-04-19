# The Oblivion Cycle - Chapter I: The Shimmering Gate
# (C)opyright 2024 RLM Productions
import functions.gameFunctions as l
import functions.heroVariables as hero
import time, os, sqlite3

#open database for Music Theme
con = sqlite3.connect('data.db')
cur = con.cursor()
result=cur.execute("select filename from music where id ='2'").fetchone()
musictrack = 'asset/'+ result[0]
con.close()
l.cursor.hide() #hides cursor
l.play_music(musictrack)
os.system('cls')
time.sleep(2.2) # for Dramatic Musical Intro

while True:
    l.titlescreen() # Load the Title Screen
    menuValue=l.title_menu(l.menuValue) # Load the Title Menu
# l.createhero() # Load Create Game

# Code for New Game
    if menuValue == '1':
        l.delay_print2('New Game selected...')
        time.sleep(2)
        l.createhero()

# Code for Load Game
    if menuValue == '2':
        l.delay_print2('Loading Game...')
        time.sleep(2)
        os.system('cls')
        break

# Code for Load Game
    if menuValue == '3':
        l.delay_print2('Options...')
        time.sleep(2)
        os.system('cls')
        break    




### MAIN CODE ####




# Game Info Dump
    if menuValue == 'i':
        l.cursor.hide()
        l.delay_print2('Game Info...\n')     
        print(l.GameInfo['GameTitle'] + ': ' + l.GameInfo['GameSubtitle'])
        print('Version: ' + l.GameInfo['GameVersion'])
        print('Copyright: ' + l.GameInfo['Copyright'])
        print('Author: ' + l.GameInfo['Author'])
        time.sleep(10)
        os.system('cls')
        break

# Battle Simulation
    if menuValue == 'b':
        l.delay_print2('Battle Preview...')
        time.sleep(2)
        os.system('cls')
        l.battle_seq()


# Quit the Game
    if menuValue == '4':
        l.delay_print2('Thanks for playing!')
        time.sleep(4)
        os.system('cls')
        break

exit(0)