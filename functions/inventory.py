import os, copy
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.progress import *

def inventory():
  custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
  console = Console(theme=custom_theme)

  # Temp Variables
  class Item:
    def __init__(self, name, attack:int, defense:int, desc, qty:int):
      self.name = name
      self.attack = attack
      self.defense = defense
      self.desc = desc
      self.qty = qty

  cloth_armor = Item("Cloth Armor", 0, 2, "A robe that covers the wearer but supplies little armor", 1)
  short_sword = Item("Short Sword",5, 0, "A small sword that deals normal damage", 1)

  real_cloth_armor = copy.deepcopy(cloth_armor)

  hero_inv = [real_cloth_armor,short_sword]
  hero_equip_armor = cloth_armor
  hero_equip_weapon = short_sword
  hero_gold = 2232 

  real_cloth_armor.qty = real_cloth_armor.qty + 5  


  os.system("cls")
  # Equipped Table
  table = Table(title="Current Equipment", title_justify="left")
  table.add_column("Type", style="normal", width=10)
  table.add_column("Item", style="normal", width=20)
  table.add_column("Atk", style="normal", width=3)
  table.add_column("Def", style="normal", width=3)

  # Equipment Definition
  table.add_row("Body","[green]"+hero_equip_armor.name+"[/green]",str(hero_equip_armor.attack),str(hero_equip_armor.defense))
  table.add_row("Weapon","[red]"+hero_equip_weapon.name+"[/red]",str(hero_equip_weapon.attack),str(hero_equip_weapon.defense))
  console.print(table)

  # Inventory Table
  table = Table(title="Inventory", title_justify="left")
  table.add_column("Item Name", style="cyan", width=25)
  table.add_column("Qty", style="normal", width=3)
  table.add_column("Description", style="normal")

  a = 1
  for i in hero_inv:
      table.add_row("[normal]"+str(a)+') [/normal]'+ i.name,str(i.qty),i.desc)
      a +=1
  console.print(table)

  # Gold Table
  table = Table()
  table.add_column("Currency", style="yellow", width=10)
  table.add_column("Qty", style="yellow", width=5)
  table.add_row("Gold",str(hero_gold))
  console.print(table)
  console.print('\n')
  console.input('Press any key to return...')