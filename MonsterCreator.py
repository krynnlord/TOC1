import os, time
import editor.create as c
import editor.viewer as v

while True:
    os.system('CLS')
    print('*******************************************')
    print('Monster Creater for The Oblivion Cycle')
    print('(C)opyright 2024 RLM Productions')
    print('*******************************************\n')
    print('(1) View Monster')
    print('(2) Create Monster')
    print('(3) Quit')

    ans = input('\nYour Choice? ') 
    if ans == '3':
        break
    if ans == '2':
        print('Creation starting....')
        c.Create()
        
    if ans == '1':
        print('Viewing Monsters....')
        v.View()

print('Exiting the program!')
time.sleep(2)
os.system('cls')