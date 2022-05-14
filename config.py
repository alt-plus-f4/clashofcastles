import pygame as pg
from pygame.math import Vector2
# from libs.database import DataBase

# db = DataBase("localhost","root","","pygame")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)

# WINDOWS PROPORTIONS
WIDTH = 1280
HEIGHT = 720

# 1280 x 720

pg.init()
pg.font.init()

gameDisplay = pg.display.set_mode((WIDTH,HEIGHT))

# PROGRAM ICON
icon = pg.image.load('assets\\icon.png')

pg.display.set_icon(icon)
pg.display.set_caption('Clash of Castles')
pg.display.update()

# Images
attack_img = pg.image.load('assets\\attack.png').convert_alpha()
shop_img = pg.image.load('assets\\shop.png').convert_alpha()
grass_img = pg.image.load('assets\\grass.png').convert_alpha()
grass2_img = pg.image.load('assets\\grass2.png').convert_alpha()
# BG
background_img = pg.image.load('assets\\background.png').convert_alpha()

# FONT
font = pg.font.Font('assets\\font.ttf', 25)

TILESIZE = WIDTH // 40

BGCOLOR = DARKGREY

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')