import random

###########################################################
# New Dice Roller Takes in string value template like 1d4 #
###########################################################
def diceroller(diceroll):
	
	total = []

	for i in range(int(diceroll[0])):
		roll = random.randrange(1, int(diceroll[2])+1)
		total.append(roll)
		final = sum(total)
	
	return final

#################################################################
# Crit Chance roller. Dice must be 20 to crit. Improved by Luck #
#################################################################
def critroller(luck):
	
	crit = 0
	roll = random.randrange((1 + luck), 21)

	if roll == 20:
		crit = 1 # Critical Strike
	elif roll == 1:
		crit = 2 # Miss
	else:
		crit = 0 # Normal Strike
	return crit

##########################
# Main Damage Calculator #
##########################
def damage_calc(luck, mod, weapon_damage):
	
	# Base Attack Value
	atk_value = diceroller(weapon_damage) + mod
	
	# Initilize Modifier and Crit(0-No 1-Yes)
	modifier_value = 0
	success_crit = 0
	
	# Roll Crit Dice
	success_crit = critroller(luck)
	
	# Result in crit or no crit
	if success_crit == 1:
		modifier_value = atk_value + mod + diceroller(weapon_damage)
	elif success_crit == 2:
		modifier_value = 0
	else:
		modifier_value = atk_value + mod

	# return value and crit value
	return modifier_value, success_crit 