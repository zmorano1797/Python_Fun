import easygui as g
import classes as h


def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
    

def CharName():
    name = False
    player1Filename = "player1.txt"
    player1 = h.player1(player1Filename)
    while name is False:
        Char_Name = g.enterbox("What's you're name young traveller?")
        if Char_Name is None:
            break
        name == is_integer(Char_Name)
        if name == is_integer(Char_Name) is True:
            g.msgbox("That's not a name", title="ErRoR", ok_button="Return")
            name = False
        else:
            if g.ynbox("Are you sure you want " + Char_Name, title="Confirmation") is True:
                name = True
                player1.Char_Name = Char_Name
                player1.store()
            else:
                name = False