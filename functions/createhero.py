import os, time, sqlite3
import functions.gameFunctions as l

def createhero():
    os.system('cls')
    filetitle = 'asset/art/createhero.dat'
    data = ''
    print(f"{l.ColorStyle.YELLOW}"+l.loadart(filetitle, data)+f"{l.ColorStyle.RESET}")
    print("\nCreating a new game. Please enter a name for your hero.")
    l.cursor.show()
    name = input('Name: ' )
    if name == '':
        l.cursor.hide()
        print('You must enter a name.')
        time.sleep(2)
        createhero()
    if len(name) < 3:
        l.cursor.hide()
        print('Your name must be 3 characters or more in length')
        time.sleep(2)
        createhero()
    #Verification on new game
    l.cursor.hide()
    shortname = name[:10]
    l.delay_print2(f'{l.ColorStyle.RED}\nWARNING: {l.ColorStyle.RESET}This will delete your current game progress!')
    l.delay_print2("\nAre you sure you want to start over as "+ f'{l.ColorStyle.YELLOW}'+shortname+f'{l.ColorStyle.RESET}' +"?")
    l.cursor.show()
    ans = input(" (Y/N) ")
    
    if ans == 'y' or ans == 'Y':
        con = sqlite3.connect('data.db')
        cur = con.cursor()

        # Write to DB - HERO
        cur.execute("update hero set name='" + shortname + "',hp=10,hp_max=10,mp=10,mp_max=10,str=10,int=10,dex=10,luck=5,DEF_m=0,DEF_s=0,DEF_b=0,level=1,exp=0,stat=1 where id=1")
        con.commit()
        con.close()
        print('New game started....')
        time.sleep(2)
        return        
    
    if ans == 'n' or ans == 'N':
        l.menuValue = '0'
        return