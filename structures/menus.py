from config import *

def shop_menu():
    rect = Rectangle(1000, 650, (232, 223, 223))
    rect.set_rounded(10)
    rect.rect.center = gameDisplay.get_rect().center
    close_button = Rectangle(30, 30, (255, 0, 0))
    close_button.set_rounded(5)
    close_button.rect.center = (1120, 55)
    menu = pg.sprite.Group([rect, close_button])
    menu.draw(gameDisplay)

def exited(shop_open):
    if(shop_open == True and pg.mouse.get_pos()[0] > 1105 and  pg.mouse.get_pos()[0] < 1135 and pg.mouse.get_pos()[1] > 40 and pg.mouse.get_pos()[1] < 70):
        return True
    return False

class Rectangle(pg.sprite.Sprite):
    def __init__(self, x, y, color):
        pg.sprite.Sprite.__init__(self)
        self.original_image = pg.Surface((x, y))
        self.original_image.fill(color)
        self.image = self.original_image
        self.rect = self.image.get_rect()

    def set_rounded(self, roundness):
        size = self.original_image.get_size()
        self.rect_image = pg.Surface(size, pg.SRCALPHA)
        pg.draw.rect(self.rect_image, (255, 255, 255), (0, 0, *size), border_radius=roundness)

        self.image = self.original_image.copy().convert_alpha()
        self.image.blit(self.rect_image, (0, 0), None, pg.BLEND_RGBA_MIN) 
    # pg.draw.rect(gameDisplay, (255, 255, 255), pg.Rect(30, 30, 60, 60),  2, 3)

class Label:
    def __init__(self, x, y, text=''):
        self.x = x
        self.y = y
        self.text = text
        self.label = font.render(text, True, (0, 0, 0))
        
    def draw(self, gameDisplay):
        gameDisplay.blit(self.label, (self.x, self.y))