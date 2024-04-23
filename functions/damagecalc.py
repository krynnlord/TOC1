import random


def hero_damage_calc(hero_stats, hero_weapon):
    
    # Attack Value is weapon attack +- 25%
    atk_value = random.randrange(round(hero_weapon - (hero_weapon * .25)), round(hero_weapon + (hero_weapon * .25)))
    
    # Initilize Modifier
    modifier_value = 0
    
    # Initilize Crit (0-No 1-Yes)
    hero_crit = 0
    
    # Player Luck chance for items. Sets luck value - 20
    luckmod = random.randrange(hero_stats.luck, 20)
    if luckmod >= 16:

        # create 3d6 for roll
        modrand1 = (random.randrange(1,6))
        modrand2 = (random.randrange(1,6))
        modrand3 = (random.randrange(1,6))
        modrand = max(modrand1,modrand2,modrand3)

        # Sets Crit Modified value
        modifier_value = round((atk_value + (modrand +2)))
        
        # Set Crit to Yes
        hero_crit = 1 

    else:
        # No Crit just normal attack
        modifier_value = atk_value 

    # return value and crit value
    return modifier_value, hero_crit 
