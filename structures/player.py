from config import *

class Player:
    def __init__(self, tag):
        self.tag = tag

    def getPlayerInfo(self):
        if(db.selectByTag(self.tag)):
            return True
        else:
            return False