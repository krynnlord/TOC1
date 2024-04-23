class spell:
    def __init__(self, name, desc, qty, ready, modifier, circle, levelreq):
        self.name = name
        self.desc = desc
        self.qty = qty
        self.ready = ready
        self.modifier = modifier # Heal or Damage
        self.circle = circle
        self.levelreq = levelreq

# Circle 1
heal = spell("Heal", "Heals for a small amount", 3, 1, 15, 1, 1)
cure = spell("Cure", "Heals for a small amount", 0, 0, 15, 1, 2)
create_food = spell("Create Food", "Heals for a small amount", 0, 0, 15, 1, 3)
magic_missle = spell("Magic Missle", "Heals for a small amount", 0, 0, 15, 1, 4)

# Circle 2
greater_heal = spell("Greater Heal", "Heals for a small amount", 0, 0, 15, 2, 5)
barrier = spell("Barrier", "Creates a protective barrier around user", 0, 0, 1, 2, 6)
escape = spell("Escape", "Heals for a small amount", 0, 0, 15, 2, 7)
fireball = spell("Fireball","Sends a hurl of fire at opponent.", 2, 1, 25, 2, 8)

# Circle 3
regeneration = spell("Regeneration", "Heals for a small amount", 0, 0, 15, 3, 9)
holy_ground = spell("Holy Ground", "Heals for a small amount", 0, 0, 15, 3, 10)
double = spell("Double", "Heals for a small amount", 0, 0, 15, 3, 11)
immolation = spell("Immolation", "Heals for a small amount", 0, 0, 15, 3, 12)

hero_spells = [heal, cure, create_food, magic_missle, greater_heal, barrier, escape, fireball, regeneration, holy_ground, double, immolation]