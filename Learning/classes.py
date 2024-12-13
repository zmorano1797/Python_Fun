import easygui as g


#defineing initial character values
class player1(g.EgStore): #define player as subclass of EgStore
        def __init__(self, filename): #filename is required
                self.Char_Name = ""
                self.Health = 0
                self.Mana = 0
                self.Armor = 0
                self.filename =  filename #filename and restore are required
                self.restore()