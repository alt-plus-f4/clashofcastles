from config import *

class Buttons:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_width()
        self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        if(self.is_hovered()):
            if(pg.mouse.get_pressed()[0] == 1 and self.clicked == False):
                self.clicked = True
                action = True

        if(pg.mouse.get_pressed()[0] == 0):
            self.clicked = False

        gameDisplay.blit(self.image, (self.rect.x, self.rect.y))

        return action
    def is_hovered(self):
        pos = pg.mouse.get_pos()

        if(self.rect.collidepoint(pos)):
            return True

        return False