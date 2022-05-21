from config import *

class Player:
    def __init__(self, tag):
        self.tag = tag

    def getPlayerInfo(self):
        return db.selectByTag(self.tag)

    # TODO
    
    def save_progress(self):
        pass