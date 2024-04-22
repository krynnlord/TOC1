import os, copy
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.progress import *

def spellbook():
    custom_theme = Theme({"normal": "white", "green": "green","red": "red", "yellow": "yellow"})
    console = Console(theme=custom_theme)

    os.system("cls")

    table = Table(title="Spellbook", padding=(0, 0), width=85, title_justify='left')
    table.add_column("[red]Spells of the Magi[/red]", justify='left')
    table.add_column("[yellow]Lore[/yellow]", justify='left', style='normal')

    st = Table(
        padding=(0, 0),
        show_edge=False,
        show_lines=False,
    )
    st.add_column("Name", width=15, justify='left', style='cyan' )
    st.add_column("Circle", justify='center')
    st.add_column("Min Lvl", justify='center')
    st.add_column('Learned',justify='center')
    st.add_row('Heal', '1','1', '[green]Y[/green]')
    st.add_row('Cure', '1', '2','[red]N[/red]')
    st.add_row('Create Food', '1','3', '[red]N[/red]')
    st.add_row('Magic Missle', '1','4', '[red]N[/red]')
    st.add_row('Greater Heal', '2','5', '[red]N[/red]')
    st.add_row('Barrier', '2','6', '[red]N[/red]')
    st.add_row('Escape', '2', '7','[red]N[/red]')
    st.add_row('Fireball', '2', '8','[red]N[/red]')
    st.add_row('Regeneration', '3','9', '[red]N[/red]')
    st.add_row('Holy Ground', '3', '10','[red]N[/red]')
    st.add_row('Double', '3', '11','[red]N[/red]')
    st.add_row('Immolation', '3', '12','[red]N[/red]')

    tt="The spells of the Magi are composed of 3 circles. Each of these circles has 4 spells from each of the dispiplines. These are Invocation, Abjuration, Conjuration, and Evocation.\n\nInvocation is the study of healing spells. Abjuration focuses on protective magic. Conjuration creates objects, and Evocation is the destructive arts. Master each of these displines in their respective circles to become one with the elements.\n\n- Magnus Dylisia"
    table.add_row(st, tt)
    console.print(table)

    console.input('Press any key to return...')