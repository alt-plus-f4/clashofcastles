# from pygame import MOUSEWHEEL
from structures.map import Map
from config import *

class Level:
    def __init__(self, arr):
        self.arr = Map(arr)
        self.x = 0



    #! USED ONLY FIRST TIME FOR PRERENDERING NOW I DONT NEED IT


    # def getMap(self):
    #     self.blockmap = pg.sprite.Group()

    #     # for row in self.arr: 
    #     for row in range(0, 64): 
    #         for col in range(0, 36):
    #             # if tile == '1':
    #             #     gameDisplay.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
    #             # if tile == 0:
    #             if col % 2 == 0:
    #                 if row % 2 == 0:
    #                     self.blockmap.add(Tile(grass_img, row * TILESIZE, col * TILESIZE))
    #                 else:
    #                     self.blockmap.add(Tile(grass2_img, row * TILESIZE, col * TILESIZE))
    #             else:
    #                 if row % 2 == 0:
    #                     self.blockmap.add(Tile(grass2_img, row * TILESIZE, col * TILESIZE))
    #                 else:
    #                     self.blockmap.add(Tile(grass_img, row * TILESIZE, col * TILESIZE))
    #             # if tile != '0':
    #             #     tile_rects.append(pg.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE))

    def draw(self):
        # self.getMap()
        # for item in self.blockmap:
        #     item.draw()
        gameDisplay.blit(background_img, (0,0))

    def handle_event(self, open):
        if(open == True and pg.mouse.get_pos() == (0, 0)):
            print("oa")
        # ADD MOVING WITH ARROW KEYS
        # for item in self.blockmap:
        #     item.move()
        # gameDisplay.blit(pg.transform.scale(background_img, (WIDTH + self.x, HEIGHT + self.x)), (0, 0))

class Tile(pg.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
    def draw(self):
        gameDisplay.blit(self.image, (self.x, self.y))
    def move(self):
        gameDisplay.blit(self.image, (self.x))