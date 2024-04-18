import os, sqlite3, time

monstername = ''
monster = {
    'id' : 0,
    'name' : monstername,
    'LEVEL' : 0,
    'HP' : 0,
    'HP_MAX' : 0,
    'MP' : 0,
    'MP_MAX' : 0,
    'ATK' : 0,
    'DEF' : 0,
    'TYPE': 0,
    }

def View():
    os.system('cls')
    print('*******************************************')
    print('View Monsters')
    print('*******************************************\n')
    print('(1) View by Name')
    print('(2) View by Level')
    print('(3) Return to Main Menu')

    while True:
        ans = input('\nYour Choice? ') 
        if ans == '1':
            name = input('Name: ')
            print("----------------- RECORD SCHEME --------------------")
            print('(ID,name,hp,hp_max,mp,mp_max,level,atk,def,type)')
            print("----------------------------------------------------")
            con = sqlite3.connect('data.db')
            cur = con.cursor()
            result =(cur.execute("select * from character where name like '%'||?||'%' order by id",(name,)))
            while True:
                output = result.fetchone()
                if output == None:
                    break
                print(output)
            con.close()
            
            ans = input('\nPress any key to return')
            break
        
            
        if ans == '2':
            level = input('Level: ')
            print("----------------- RECORD SCHEME --------------------")
            print('(ID,name,hp,hp_max,mp,mp_max,level,atk,def,type)')
            print("----------------------------------------------------")
            con = sqlite3.connect('data.db')
            cur = con.cursor()
            result =(cur.execute("select * from character where level = ? order by id",(level,)))
            
            while True:
                output = result.fetchone()
                if output == None:
                    break
                print(output)
            con.close()
            ans = input('\nPress any key to return!')
            break

        if ans == '3':
            break