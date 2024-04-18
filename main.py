# The Oblivion Cycle - Chapter I: The Shimmering Gate
# (C)opyright 2024 RLM Productions
import functions.gameFunctions as l
import functions.heroVariables as hero
import time, os

menuValue = '0'
l.titlescreen() # Load the Title Screen
menuValue=l.title_menu(menuValue) # Load the Title Menu


# Code for New Game
if menuValue == '1':
    l.delay_print2('New Game selected...')
    time.sleep(2)


# Code for Load Game
if menuValue == '2':
    l.delay_print2('Loading Game...')
    time.sleep(2)
    

# Game Info Dump
if menuValue == '4':
    l.delay_print2('Game Info...')
    time.sleep(2)
    os.system('cls')
    print('\nGame: ' + l.GameInfo['GameTitle'] + ': ' + l.GameInfo['GameSubtitle'])
    print('Version: ' + l.GameInfo['GameVersion'])
    print('Copyright: ' + l.GameInfo['Copyright'])
    print('Author: ' + l.GameInfo['Author'])


# Quit the Game
if menuValue == '3':
    l.delay_print2('Goodbye!')
    time.sleep(2)
    exit(0)
