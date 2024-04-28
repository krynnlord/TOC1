from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
console = Console(theme=custom_theme, highlight=None)

def hero_status_bar(hero):
    for i in range(90):
        console.print ("-", end="")
    console.print("\n[white]"+hero[0].name + "   Level: " + str(hero[0].level) + "   Exp: " + str(hero[0].exp)+"[/white]", end="   ")
    console.print("[white]Armor: " + hero[1].name + "   Weapon: " + hero[2].name+"[/white]", end="   ")
    console.print("Gold: " + str(hero[0].gold))
    for i in range(90):
        console.print ("-", end="")
    console.print("\n")
