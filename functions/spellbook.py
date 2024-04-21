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
    table.add_column("[red]Spells of the Magi[/red]", justify='center')
    table.add_column("[yellow]Lore[/yellow]", justify='center', style='normal')

    st = Table(
        padding=(0, 0),
        show_edge=False,
        show_lines=False,
    )
    st.add_column("Name", width=15, justify='left', style='cyan' )
    st.add_column("Cir", justify='center')
    st.add_column("Min", justify='center')
    st.add_column('Lrnd',justify='center')
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

    tt="Enchantments that can be applied to multiple (but not all) weapons will be listed under every weapon that can obtain the enchantment and marked in bold. (As there are several enchantments that can be applied to “any sword” or similar.) For the sake of completion there will be a “generic enchantments” list for enchantments that can be applied to any weapon or are too broad to be listed under every weapon. (Example: only one-handed weapons, only melee weapons, only ranged weapons, etc.)')"
    table.add_row(st, tt)
    console.print(table)

    console.input('Press any key to return...')