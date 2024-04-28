import os
import time,msvcrt
import functions.gameFunctions as l
import keyboard, cursor

# Intro to Game
def intro():
                 
    l.cursor.hide() #hides cursor

    os.system('cls')
    time.sleep(2.2) # pause for Dramatic Musical Intro

    # Load RLM Productions Logo
    filetitle = 'asset/art/rlm.dat'
    data = ''    
    print(f"{l.ColorStyle.YELLOW}"+l.loadart(filetitle, data)+f"{l.ColorStyle.RESET}")
    for i in range(54):
        print(" ", end="")
    time.sleep(2)    
    l.delay_print("presents an original game")
    time.sleep(5)

    # Main Logo Display
    filetitle = 'asset/art/title.dat'
    data = ''
    os.system('cls')
    print(f"{l.ColorStyle.RED}"+l.loadart(filetitle, data)+f"{l.ColorStyle.RESET}")
    time.sleep(2)
    l.delay_print("                          Chapter I: The Shimmering Gate")
    time.sleep(2)
    l.delay_print("\n\nOur story begins in a kingdom just south of the mighty river Hyatin,\n")
    l.delay_print("known for its production of a special mineral name Shieya.\n\n")
    time.sleep(1)
    l.delay_print("This mineral has an unique property that many nations seek, and is coveted beyond\n")
    l.delay_print("measure to the point where many are willing to kill for it.\n\n")
    time.sleep(1)
    l.delay_print("In these trying times a hero emerges....")
    time.sleep(4)