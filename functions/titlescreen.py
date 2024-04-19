import os
import time,msvcrt
import functions.gameFunctions as l
import keyboard, cursor

# Title Screen
def titlescreen():
    
    filetitle = 'asset/title.dat'
    data = ''
    os.system('cls')
    print(f"{l.ColorStyle.RED}"+l.loadart(filetitle, data)+f"{l.ColorStyle.RESET}")
    time.sleep(2)
    l.delay_print("                          Chapter I: The Shimmering Gate")
    time.sleep(2)
    print('')

# Title Menu
def title_menu(menuValuea):
    print('')
    l.delay_print2('(' + f'{l.ColorStyle.YELLOW}1{l.ColorStyle.RESET}' + ') New Game\n')
    l.delay_print2('(' + f'{l.ColorStyle.YELLOW}2{l.ColorStyle.RESET}' + ') Load Game\n')
    l.delay_print2('(' + f'{l.ColorStyle.YELLOW}3{l.ColorStyle.RESET}' + ') Options\n')
    l.delay_print2('(' + f'{l.ColorStyle.YELLOW}4{l.ColorStyle.RESET}' + ') Quit Game\n')
    print('')
    print("", end="\r")

    while True:
        if keyboard.is_pressed("4"):
            menuValuea = '4'
            l.play_sound('asset/button_press.wav')
            msvcrt.getch() # Clears Input
            return menuValuea
        if keyboard.is_pressed("1"):
            menuValuea = '1'
            l.play_sound('asset/button_press.wav')
            msvcrt.getch()
            return menuValuea
        if keyboard.is_pressed("2"):
            menuValuea = '2'
            l.play_sound('asset/button_press.wav')
            msvcrt.getch()
            return menuValuea
        if keyboard.is_pressed("i"):
            menuValuea = 'i'
            l.play_sound('asset/button_press.wav')
            msvcrt.getch()
            return menuValuea
        if keyboard.is_pressed("3"):
            menuValuea = '3'
            l.play_sound('asset/button_press.wav')
            msvcrt.getch()
            return menuValuea