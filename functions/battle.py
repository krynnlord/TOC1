import os, random 
import functions.gameFunctions as l

def battle_seq():
    # Define Hero
    hero_class = {'name' : '', 'HP' : 0, 'HP_max': 0, 'MP' : 0, 'MP_max' : 0, 'luck': 0,'level' : 0}
    hero = hero_class
    hero['name'] = 'Avatar'
    hero['level'] = 4
    hero['HP'] = 200
    hero['HP_max'] = 200
    hero['MP'] = 100
    hero['MP_max']  = 100
    hero['luck'] = 2

    # Hero Equiped
    equipment = {'weapon' : '', 'armor' :'' }
    hero_equip = equipment
    hero_equip['weapon'] = 'Short Sword'
    hero_equip['armor'] = 'Cloth Armor'

    # Define Enemy 
    enemy = {'name' : '', 'HP' : 0, 'HP_max': 0, 'MP' : 0, 'MP_max' : 0, 'luck' : 0, 'level': 0}
    enemy_current = enemy
    enemy_current['name'] = 'Ghoul'
    enemy_current['level'] = 1
    enemy_current['HP'] = 200
    enemy_current['HP_max'] = 200
    enemy_current['MP'] = 0
    enemy_current['MP_max']  = 0
    enemy_current['luck'] = 1

    # Battle Strings
    hero_combat_string = "Ready for Combat."
    enemy_combat_string = "Ready for Combat."

    # Combat Active
    endcombat = False

    # Battle Loop
    while True:

        # Hero Display
        os.system('cls')
        hero_disp_hp = (str(hero['HP'])+'/'+ str(hero['HP_max']))
        hero_disp_mp = (str(hero['MP'])+'/'+ str(hero['MP_max']))
        print(f"{l.ColorStyle.GREEN}___ PLAYER __________________________________ LEVEL: " +str(hero['level'])+ f"{l.ColorStyle.RESET}\n")
        print("Name: "+hero['name'].ljust(15)+"HP: "+hero_disp_hp.ljust(14)+"MP: "+hero_disp_mp)

        # Print HERO Health Bars
        hp_bar = ""
        if hero['HP_max'] == 0:
            bar_ticks = 0
        else:
            bar_ticks = (hero['HP'] / hero['HP_max']) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        blankspace = '                     '
        print(blankspace, end='')
        print(f"{l.ColorStyle.GREEN}"+hp_bar.ljust(18)+f"{l.ColorStyle.RESET}",end='' )

        # print HERO Manabar
        mp_bar = ""
        if hero['MP_max'] == 0:
            bar_ticks = 0
        else:
            bar_ticks = (hero['MP'] / hero['MP_max']) * 100 / 10

        while bar_ticks > 0:
            mp_bar += "█"
            bar_ticks -= 1
        print(f"{l.ColorStyle.BLUE}"+mp_bar+f"{l.ColorStyle.RESET}",end='' )


        # Enemy Display
        print('\n')
        enemy_disp_hp = (str(enemy_current['HP'])+'/'+ str(enemy_current['HP_max']))
        enemy_disp_mp = (str(enemy_current['MP'])+'/'+ str(enemy_current['MP_max']))
        print(f"{l.ColorStyle.RED}___ ENEMY ___________________________________ LEVEL: " +str(enemy_current['level'])+ f"{l.ColorStyle.RESET}\n")
        print("Name: "+enemy_current['name'].ljust(15)+"HP: "+enemy_disp_hp.ljust(14)+"MP: "+enemy_disp_mp)

        # Print ENEMY Health Bars
        hp_bar = ""
        if enemy_current['HP_max'] == 0:
            bar_ticks = 0
        else:
            bar_ticks = (enemy_current['HP'] / enemy_current['HP_max']) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        blankspace = '                     '
        print(blankspace, end='')
        print(f"{l.ColorStyle.GREEN}"+hp_bar.ljust(18)+f"{l.ColorStyle.RESET}",end='' )

        # print ENEMY Manabar
        mp_bar = ""
        if enemy_current['MP_max'] == 0:
            bar_ticks = 0
        else:
            bar_ticks = (enemy_current['MP'] / enemy_current['MP_max']) * 100 / 10

        while bar_ticks > 0:
            mp_bar += "█"
            bar_ticks -= 1
        print(f"{l.ColorStyle.BLUE}"+mp_bar+f"{l.ColorStyle.RESET}",end='' )


        # Battle Log Display
        print('\n')
        print("___ COMBAT LOG _______________________________________\n")
        l.delay_print2(f"{l.ColorStyle.GREEN}"+hero['name']+f"{l.ColorStyle.RESET}"+': '+hero_combat_string+'\n')
        l.delay_print2(f"{l.ColorStyle.RED}"+enemy_current['name']+f"{l.ColorStyle.RESET}"+': '+enemy_combat_string+'\n')


        # Actions Menu
        if endcombat == True:
            print('\n')
            print(f"{l.ColorStyle.YELLOW}<-ACTIONS->{l.ColorStyle.RESET}")        
            print(f"{l.ColorStyle.YELLOW}1{l.ColorStyle.RESET}) Exit Combat")
            ans = input('Command > ')
            break
        else:
            print('\n')
            print(f"{l.ColorStyle.YELLOW}<-ACTIONS->{l.ColorStyle.RESET}")
            print(f"{l.ColorStyle.YELLOW}1{l.ColorStyle.RESET}) Attack with " + hero_equip['weapon'])
            print(f"{l.ColorStyle.YELLOW}2{l.ColorStyle.RESET}) Cast")
            print(f"{l.ColorStyle.YELLOW}3{l.ColorStyle.RESET}) Wait")
            print(f"{l.ColorStyle.YELLOW}4{l.ColorStyle.RESET}) Inventory")
            print(f"{l.ColorStyle.YELLOW}5{l.ColorStyle.RESET}) Run")


        ans = input('Command > ')
        if ans == '1':

            # Hero Turn
            #print('You attack the '+enemy_current['name']+ ' with your sword')
            atk_value = random.randrange(0,20)
            modifier_value = 0
            hero_crit = 0
            luckmod = random.randrange(hero['luck'], 20)
            if luckmod >= 16:
                modifier_value = ((atk_value*hero['luck']) * 2)
                hero_crit = 1
            if hero_crit == 1:
                enemy_current['HP'] -= atk_value + modifier_value
            else:        
                enemy_current['HP'] -= atk_value
            if enemy_current['HP'] <= 0:
                enemy_current['HP'] = 0
                hero_combat_string = "Hits "+enemy_current['name']+ " with "+hero_equip['weapon'] +" for " + str(atk_value) +" damage, and kills it!"
                endcombat = True
            else:    
                if atk_value >= 1:
                    if hero_crit == 1:
                        hero_combat_string = "*CRITICAL* Hits "+enemy_current['name']  +" with "+hero_equip['weapon'] +" for " + str(atk_value) +" damage."
                    else:
                        hero_combat_string = "Hits "+enemy_current['name']  +" with "+hero_equip['weapon'] +" for " + str(atk_value) +" damage."
                else:
                    hero_combat_string = "misses "+enemy_current['name']  +"."
            # Enemy Turn
            #print(enemy_current['name']+' attacks you.')
            atk_value = random.randrange(0,15)
            hero['HP'] -= atk_value
            if endcombat == True:
                atk_value = 0
            if hero['HP'] <= 0:
                hero['HP'] = 0
                enemy_combat_string = enemy_current['name']+" has killed you."
                endcombat = True
            else:    
                if atk_value >= 1:
                    enemy_combat_string = "Hits " + hero['name'] +" for " + str(atk_value) +" damage."
                else:
                    if endcombat == True:
                        enemy_combat_string = "has died."  
                    else:
                        enemy_combat_string = "misses " + hero['name'] +"."


        if ans == '4':
            hero_equip['weapon'] ='Hands'
        if ans == '5':
            break    