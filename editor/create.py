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

def Create():
    os.system('cls')
    print('*******************************************')
    print('Create your monster')
    print('*******************************************\n')
    
    monster1 = monster
    monster1["id"] = input('id> ')
    monster1["name"] = input('Name> ')
    monster1["LEVEL"] = input('Level> ')
    monster1["HP_MAX"] = input('HP> ')
    monster1['HP'] = monster1['HP_MAX']
    monster1["MP_MAX"] = input('MP> ')
    monster1["MP"] = monster1["MP_MAX"]
    monster1["ATK"] = input('Attack Value> ')
    monster1["DEF"] = input('Defence Value> ')
    monster1["TYPE"] = '1'

    os.system('cls')
    print ('MONSTER REVIEW')
    print ('---------------')
    print('id: ' + monster1['id'])
    print('Name: ' + monster1['name'])
    print('Level: ' + monster1['LEVEL'])
    print('HP: ' + monster1['HP_MAX'])
    print('MP: ' + monster1['MP_MAX'])
    print('ATK: ' + monster1['ATK'])
    print('DEF: ' + monster1['DEF'])
    print('TYPE: ' + monster1['TYPE'])
    
    while True:
        ans = input('\nDoes this look Correct? ') 
        if ans == 'n' or ans == 'N':
            break
        if ans == 'y' or ans == 'Y':
            print('Writing monster to database....')

            con = sqlite3.connect('char.db')
            cur = con.cursor()

            # Write to DB
            cur.execute("insert into character(id,name,hp,hp_max,mp,mp_max,level,atk,def,type) values('" + monster1['id'] + "', '" + monster1['name'] + "', '" + monster1['HP'] + "', '" + monster1['HP_MAX'] + "', '" + monster1['MP'] + "', '" + monster1['MP_MAX'] + "', '" + monster1['LEVEL'] + "', '" + monster1['ATK'] + "', '" + monster1['DEF'] +  "', '" + monster1['TYPE'] + "')")
            con.commit()
            con.close()
            print('Success!')
            time.sleep(3)
            break