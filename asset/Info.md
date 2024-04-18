# Info-Dump for Game
*I will store ideas stored here for future projects or reference to materials already programmed.*

### This line can be called to show graphic from DAT file:
    filetitle = 'asset/castle.dat'
        data = ''
        print('')
        print(l.loadart(filetitle, data))

### Adventure Menu:
    Castle: Speak with king for Quests
    Temple: Heal, Cure, Remove Curse
    Armory: weapons, armor
    Inn: Rest, memorize spells
    Provisioner: Buy and Sell Items
    Circle of Stones: Enter the Shimmering Gate for Questing

### Example of Color Coding Text
    print(f"{l.ColorStyle.RED}"+l.loadart(filetitle, data)+f"{l.ColorStyle.RESET}")