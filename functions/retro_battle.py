import os, random 
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
import functions.gameFunctions as l

def r_battle_seq():
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
        console.print("Hero")
        for i in range(70):
            console.print("-", end="")
        console.print("\nName: " + hero1['name'], end="    ")
        console.print("Level: "+ str(hero1['level']), end="   ")
        console.print("Weapon: " + hero_equip['weapon'], end="   ")
        console.print("Armor: " + hero_equip['armor'])

        hppercent = 100 * round(hero1['HP']) / round(hero1['HP_max'])
        if hppercent >= 75:
            console.print("[green]" + str(hppercent) + '%[/green]',end="   ")
        elif hppercent < 75 and hppercent > 40:
            console.print("[yellow]" + str(hppercent) + '%[/yellow]',end="   ")
        else:
            console.print("[red]" + str(hppercent) + '%[/red]',end="   ")
        console.print("HP: " + str(hero1['HP'])+'/'+ str(hero1['HP_max']))

        # print HERO HPbar
        hp_bar = ""
        if hero1['HP_max'] == 0:
            bar_ticks = 0
        else:
            bar_ticks = (hero1['HP'] / hero1['HP_max']) * 100 / 4
        while bar_ticks > 0:
            hp_bar += ":"
            bar_ticks -= 1
        hero_line2 = (hp_bar)
        if hppercent >= 75:
            console.print("[green]"+ hero_line2 + "[/green]")
        elif hppercent < 75 and hppercent > 40:
            console.print("[yellow]" + hero_line2 + "[/yellow]")
        else:
            console.print("[red]" + hero_line2 + "[/red]")
        
        console.print("\n")
        
        # Enemy Display
        console.print("Enemy")
        for i in range(70):
            console.print("-", end="")
        console.print("\nName: " + enemy_current['name'], end="    ")
        console.print("Level: "+ str(enemy_current['level']), end="\n")
        
        hppercent_e = 100 * round(enemy_current['HP']) / round(enemy_current['HP_max'])
        if hppercent_e >= 75:
            console.print("[green]" + str(hppercent_e) + '%[/green]',end="   ")
        elif hppercent_e < 75 and hppercent_e > 40:
            console.print("[yellow]" + str(hppercent_e) + '%[/yellow]',end="   ")
        else:
            console.print("[red]" + str(hppercent_e) + '%[/red]',end="   ")
        console.print("HP: " + str(enemy_current['HP'])+'/'+ str(enemy_current['HP_max']))
        
        # print Enemy HPbar
        hp_bar = ""
        if enemy_current['HP_max'] == 0:
            bar_ticks = 0
        else:
            bar_ticks = (enemy_current['HP'] / enemy_current['HP_max']) * 100 / 4
        while bar_ticks > 0:
            hp_bar += ":"
            bar_ticks -= 1
        enemy_line2 = (hp_bar)
        if hppercent_e >= 75:
            console.print("[green]"+ enemy_line2 + "[/green]")
        elif hppercent_e < 75 and hppercent_e > 40:
            console.print("[yellow]" + enemy_line2 + "[/yellow]")
        else:
            console.print("[red]" + enemy_line2 + "[/red]")
        
        console.print("\n")
  
        # Attack Sounds
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
        console.print("Battle Log")
        for i in range(70):
            console.print("-", end="")       
        hero_combat_string = ("\n[green]"+hero1['name']+'[/green]: ' + hero_combat_string+'\n')          
        enemy_combat_string = ("[red]"+ enemy_current['name']+'[/red]: '+enemy_combat_string)
        console.print(hero_combat_string+enemy_combat_string, end="\n\n")

        # Actions Menu
        if endcombat == True:
            #console.print('\n')
            console.print("ACTIONS", style="bold underline yellow")        
            console.print("1) Exit Combat")
            ans = input('\nCommand > ')
            # l.play_music("asset/music/11.ogg",.5)
            break
        else:
            #console.print('\n')
            console.print("ACTIONS", style="bold underline yellow")
            console.print("1) Attack")
            console.print("2) Spellbook")
            console.print("3) Inventory")
            console.print("4) Run")


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