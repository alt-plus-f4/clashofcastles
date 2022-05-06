from config import *

class Label:
    def __init__(self, x, y, text=''):
        self.x = x
        self.y = y
        self.text = text
        self.label = font.render(text, True, (255,255,255))
        
    def draw(self, gameDisplay):
        gameDisplay.blit(self.label, (self.x, self.y))