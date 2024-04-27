import os
import time,msvcrt
import functions.gameFunctions as l
import keyboard, cursor

# Intro to Game
def intro():
                 
    l.cursor.hide() #hides cursor

    os.system('cls')
    time.sleep(2.2) # pause for Dramatic Musical Intro

    # Logo Display
    filetitle = 'asset/art/title.dat'
    data = ''
    os.system('cls')
    print(f"{l.ColorStyle.RED}"+l.loadart(filetitle, data)+f"{l.ColorStyle.RESET}")
    time.sleep(2)
    l.delay_print("                          Chapter I: The Shimmering Gate")
    time.sleep(2)