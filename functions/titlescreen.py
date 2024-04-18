import os
import time,msvcrt
import functions.gameFunctions as l
import keyboard

# Title Screen
def titlescreen():
    filetitle = 'asset/title.dat'
    data = ''
    os.system('cls')
    print(f"{l.ColorStyle.RED}"+l.loadart(filetitle, data)+f"{l.ColorStyle.RESET}")
    time.sleep(2)
    l.delay_print("                         Chapter I: The Shimmering Gate")
    time.sleep(4)
    print('')

# Title Menu
def title_menu(menuValuea):
    print('')
    l.delay_print2('(' + f'{l.ColorStyle.YELLOW}N{l.ColorStyle.RESET}' + ')ew Game\n')
    l.delay_print2('(' + f'{l.ColorStyle.YELLOW}L{l.ColorStyle.RESET}' + ')oad Game\n')
    l.delay_print2('(' + f'{l.ColorStyle.YELLOW}Q{l.ColorStyle.RESET}' + ')uit Game\n')
    print('')
    print("", end="\r")

    while True:
        if keyboard.is_pressed("q"):
            menuValuea = '3'
            l.play_sound('asset/button_press.wav')
            msvcrt.getch() # Clears Input
            return menuValuea
        if keyboard.is_pressed("n"):
            menuValuea = '1'
            l.play_sound('asset/button_press.wav')
            msvcrt.getch()
            return menuValuea
        if keyboard.is_pressed("l"):
            menuValuea = '2'
            l.play_sound('asset/button_press.wav')
            msvcrt.getch()
            return menuValuea
        if keyboard.is_pressed("i"):
            menuValuea = '4'
            l.play_sound('asset/button_press.wav')
            msvcrt.getch()
            return menuValuea