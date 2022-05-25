from config import *

class Player:
    def __init__(self, tag):
        self.tag = tag

    def __repr__(self):
        return self.tag
    
    def __str__(self):
        return str(self.tag)
