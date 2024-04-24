##############################################################
# Level-Up Calculator - Takes exp - sends new level and prof #
##############################################################

def checklevelup(level, prof, exp):
	 
    if exp >= 300 and exp < 900:
        level = 2
        prof = 4
    if exp >= 900 and exp < 2700:
        level = 3
        prof = 6
    if exp >= 2700 and exp < 6500:
        level = 4
        prof = 8
    if exp >= 6500 and exp < 14000:
        level = 5
        prof = 11
    if exp >= 14000 and exp < 23000:
        level = 6
        prof = 14
    if exp >= 23000 and exp < 34000:
        level = 7
        prof = 17
    if exp >= 34000 and exp < 48000:
        level = 8
        prof = 20
    if exp >= 48000 and exp < 64000:
        level = 9
        prof = 24
    if exp >= 64000 and exp < 85000:
        level = 10
        prof = 28
    if exp >= 85000 and exp < 100000:
        level = 11
        prof = 32
    if exp >= 100000 and exp < 120000:
        level = 12
        prof = 36
    if exp >= 120000 and exp < 140000:
        level = 13
        prof = 41    
    if exp >= 140000 and exp < 165000:
        level = 14
        prof = 46
    if exp >= 165000 and exp < 195000:
        level = 15
        prof = 51
    if exp >= 195000 and exp < 225000:
        level = 16
        prof = 56
    if exp >= 225000 and exp < 265000:
        level = 17
        prof = 62
    if exp >= 265000 and exp < 305000:
        level = 18
        prof = 68
    if exp >= 305000 and exp < 355000:
        level = 19
        prof = 74
    if exp > 355000:
        level = 20
        prof = 80
            
    return level, prof