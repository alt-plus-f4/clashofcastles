from config import *

class Label:
    def __init__(self, x, y, text=''):
        self.x = x
        self.y = y
        self.text = text
        self.label = font.render(text, True, (0, 0, 0))
        
    def draw(self, gameDisplay):
        gameDisplay.blit(self.label, (self.x, self.y))

class DynLabel:
    def __init__(self, x, y, color, toggle, text=''):
        self.x = x
        self.y = y
        self.text = text
        if(toggle == True):
            self.label = small_font.render(text, True, color)
        elif(toggle == False):
            self.label = font.render(text, True, color)
        else:
            self.label = big_font.render(text, True, color)
        gameDisplay.blit(self.label, (self.x, self.y))