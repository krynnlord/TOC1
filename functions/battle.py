import os, random 
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
import functions.gameFunctions as l

def battle_seq():
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme, highlight=None)

    # Define Hero
    hero_class = {'name' : '', 'HP' : 0, 'HP_max': 0, 'MP' : 0, 'MP_max' : 0, 'luck': 0,'level' : 0}
    hero1 = hero_class
    hero1['name'] = 'Kyrnnlord'
    hero1['level'] = 4
    hero1['HP'] = 200
    hero1['HP_max'] = 200
    hero1['MP'] = 100
    hero1['MP_max']  = 100
    hero1['luck'] = 2

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

    # Set Sounds *** 0-MISS 1-HIT 2-KILL 3-CRIT 4-NONE
    hitmiss = 4
    hitmiss_e = 4
    # l.play_music("asset/music/11.ogg",.5)

    # Battle Loop


    while True:

        os.system('cls')

        # Hero Display
        table = Table(title='Player', title_justify='left', style='green')
        hero_table_line = ("Name                   Level: "+ str(hero1['level']))
        table.add_column(hero_table_line, width = 35)
        hero_disp_hp = (str(hero1['HP'])+'/'+ str(hero1['HP_max']))
        hero_line1 = (hero1['name'])

        table.add_column("HP: " + hero_disp_hp, width = 25)


        # print HERO HPbar
        hp_bar = ""
        if hero1['HP_max'] == 0:
            bar_ticks = 0
        else:
            bar_ticks = (hero1['HP'] / hero1['HP_max']) * 100 / 4
        while bar_ticks > 0:
            hp_bar += "[green]█[/green]"
            bar_ticks -= 1
        hero_line2 = (hp_bar)

        # Create Hero Table
        table.add_row(hero_line1,hero_line2)
        console.print(table)

        # Enemy Display
        table = Table(title = 'Enemy', title_justify='left', style="red")
        enemy_table_line = ("Name                   Level: "+ str(enemy_current['level']))
        table.add_column(enemy_table_line, width = 35)

        enemy_disp_hp = (str(enemy_current['HP'])+'/'+ str(enemy_current['HP_max']))
        enemy_line1 = (enemy_current['name'])

        table.add_column("HP: " + enemy_disp_hp, width = 25)

        # print HERO HPbar
        hp_bar = ""
        if enemy_current['HP_max'] == 0:
            bar_ticks = 0
        else:
            bar_ticks = (enemy_current['HP'] / enemy_current['HP_max']) * 100 / 4
        while bar_ticks > 0:
            hp_bar += "[green]█[/green]"
            bar_ticks -= 1
        enemy_line2 = (hp_bar)

        # Create Enemy Table
        table.add_row(enemy_line1,enemy_line2)
        console.print(table)

        # Setup Battle Log Table
        table = Table(title ='Battle Log:', style="white", title_justify="left", width=75)
        table.add_column("[yellow]Combat[/yellow]")
        if hitmiss == 1: 
            l.play_sound('asset/sounds/hit.wav')
        if hitmiss == 0:
            l.play_sound('asset/sounds/miss.wav')
        if hitmiss == 2:
            l.play_sound('asset/sounds/kill.wav')
        if hitmiss == 3:
            l.play_sound('asset/sounds/crit.wav')       
        if hitmiss_e == 1:
            l.play_sound('asset/sounds/hit.wav')
        if hitmiss_e == 2:
            l.play_sound('asset/sounds/kill.wav')
        if hitmiss_e == 0:
            l.play_sound('asset/sounds/miss.wav')
        if hitmiss_e == 3:
            l.play_sound('asset/sounds/crit.wav') 
        
        # Print the combat strings    
        hero_combat_string = ("[green]"+hero1['name']+'[/green]: ' + hero_combat_string+'\n')          
        enemy_combat_string = ("[red]"+ enemy_current['name']+'[/red]: '+enemy_combat_string)
        
        table.add_row(hero_combat_string+enemy_combat_string)
        console.print(table)
        
        # Actions Menu
        if endcombat == True:
            #console.print('\n')
            console.print("ACTIONS", style="bold underline")        
            console.print("1) :door: Exit Combat")
            ans = input('\nCommand > ')
            # l.play_music("asset/music/11.ogg",.5)
            break
        else:
            #console.print('\n')
            console.print("ACTIONS", style="bold underline red")
            console.print("1) :dagger:  Attack with " + hero_equip['weapon'])
            console.print("2) :sparkler: Spellbook")
            console.print("3) :handbag: Inventory")
            console.print("4) :runner: Run")


        ans = input('\nCommand > ')
        if ans == '1' or ' ':

            # Hero Turn
            atk_value = random.randrange(0,20)
            modifier_value = 0
            hero_crit = 0
            luckmod = random.randrange(hero1['luck'], 20)
            if luckmod >= 16:
                modifier_value = round((atk_value*hero1['luck']) * 1.1)
                hero_crit = 1
            if hero_crit == 1:
                enemy_current['HP'] -= atk_value + modifier_value
            else:        
                enemy_current['HP'] -= atk_value
            if enemy_current['HP'] <= 0:
                enemy_current['HP'] = 0
                hero_combat_string = "Hits "+enemy_current['name']+ " with "+hero_equip['weapon'] +" for " + str(atk_value) +" damage, and kills it!"
                hitmiss = 2
                endcombat = True
            else:    
                if atk_value >= 1:
                    if hero_crit == 1:
                        hero_combat_string = "*CRITICAL* Hits "+enemy_current['name']  +" with "+hero_equip['weapon'] +" for " + str(atk_value+ modifier_value) +" damage."
                        hitmiss = 3
                    else:
                        hero_combat_string = "Hits "+enemy_current['name']  +" with "+hero_equip['weapon'] +" for " + str(atk_value) +" damage."
                        hitmiss = 1
                else:
                    hero_combat_string = "misses "+enemy_current['name']  +"."
                    hitmiss = 0
            # Enemy Turn
            #print(enemy_current['name']+' attacks you.')
            atk_value = random.randrange(0,15)
            hero1['HP'] -= atk_value
            if endcombat == True:
                atk_value = 0
            if hero1['HP'] <= 0:
                hero1['HP'] = 0
                enemy_combat_string = enemy_current['name']+" has killed you."
                endcombat = True
            else:    
                if atk_value >= 1:
                    enemy_combat_string = "Hits " + hero1['name'] +" for " + str(atk_value) +" damage."
                else:
                    if endcombat == True:
                        enemy_combat_string = "Dead."
                    else:
                        enemy_combat_string = "misses " + hero1['name'] +"."

        if ans == '2':
            l.spellbook()
            hitmiss = 4
        if ans == '3':
            l.inventory()
            hitmiss = 4
        if ans == '4':
            endcombat = True
            hitmiss = 4