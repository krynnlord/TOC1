# Define player class
class player:
    def __init__(self, name, hp, hp_max, luck, DEF_m, DEF_s, DEF_b, level, mod, exp, stat):
        self.name = name
        self.hp = hp
        self.hp_max = hp_max
        self.luck = luck
        self.DEF_m = DEF_m
        self.DEF_s = DEF_s
        self.DEF_b = DEF_b
        self.level = level
        self.mod = mod
        self.exp = exp
        self.stat = stat
        
hero = player('Krynnlord', 100, 100, 0, 0, 0, 0, 1, 2, 0, 1)