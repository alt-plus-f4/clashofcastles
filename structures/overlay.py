from config import *

class Resourses:
    def __init__(self, count):
        self.render = []
        self.count = count
        self.type = 'ELI'

    def draw(self):
        for count in count:
            if(self.type == 'ELI'):
                gameDisplay.blit(elixir_img, (0,0), self.rect)
                self.type = 'GOL'
            