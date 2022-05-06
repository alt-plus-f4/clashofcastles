from re import X
from pygame import MOUSEWHEEL
from config import *

class Level:
    def __init__(self, arr):
        self.arr = arr
        self.x = 0

    def draw_grid(self):
        for i in range(0, len(self.arr)):
            self.arr[i] = 0
        for x in range(0, len(self.arr)):
            if self.arr[x] == 0:
                pg.draw.line(gameDisplay, LIGHTGREY, (x * TILESIZE, 0), (x * TILESIZE, HEIGHT))
            else:
                pg.draw.line(gameDisplay, LIGHTGREY, (x * TILESIZE, 0), (x * TILESIZE, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            # if is building:
            pg.draw.line(gameDisplay, LIGHTGREY, (0, y), (WIDTH, y))
    def draw(self):
        gameDisplay.blit(pg.transform.scale(background_img, (WIDTH, HEIGHT)), (0, 0))
        self.draw_grid()

    def handle_event(self, event):
        if event.type == MOUSEWHEEL:
            self.x += (event.x + event.y) * 10

            gameDisplay.blit(pg.transform.scale(background_img, (WIDTH + self.x, HEIGHT + self.x)), (0, 0))
        self.draw_grid()