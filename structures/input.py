from config import *
from random import randint

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    if self.text:
                        if(db.selectByTag(self.text)):
                            print(self.text)
                            return self.text
                        else:
                            print("Not ok")
                        self.text = ''
                    else:
                        tag = randint(100000, 999999)

                        whole, row = [], []
                        i, j = 0, 0
                        for i in range(0, 36):
                            row = []
                            for j in range(0,64):
                                row.append(1)
                            whole.append(row)
                        

                        db.insert(whole, 1000, 1000, tag)

                        print(tag)

                        return tag

                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]

                else:
                    if(len(self.text) < 6):
                        self.text += event.unicode

                self.txt_surface = font.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, gameDisplay):
        gameDisplay.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(gameDisplay, self.color, self.rect, 2)