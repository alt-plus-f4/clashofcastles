from turtle import width
import pygame as pg

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
cannon_img = pg.image.load('assets\\cannon.png').convert_alpha()
wall_img = pg.image.load('assets\\wall.png').convert_alpha()
elixir_img = pg.image.load('assets\\elixir.png').convert_alpha()
coin_img = pg.image.load('assets\\coin.png').convert_alpha()
wall_img_ig = pg.image.load('assets\\wall-ig.png').convert_alpha()
cannon_img_ig = pg.image.load('assets\\cannon-ig.png').convert_alpha()

# If there was a better way .. there is for sure just I can't find one
resource_e_low_img = pg.image.load('assets\\resource-low.png').convert_alpha()
resource_e_mid_img = pg.image.load('assets\\resource-mid.png').convert_alpha()
resource_e_full_img = pg.image.load('assets\\resource-full.png').convert_alpha()
resource_g_low_img = pg.image.load('assets\\resource-g-low.png').convert_alpha()
resource_g_mid_img = pg.image.load('assets\\resource-g-mid.png').convert_alpha()
resource_g_full_img = pg.image.load('assets\\resource-g-full.png').convert_alpha()

# BG 
background_img = pg.image.load('assets\\background_rendered.png').convert_alpha()

# FONT
font = pg.font.Font('assets\\font.ttf', 25)
small_font = pg.font.Font('assets\\font.ttf', 10)
# TRANSLATE
cannon_img_ig = pg.transform.scale(cannon_img_ig, (cannon_img.get_width() // 5, cannon_img.get_height() // 5))
wall_img_ig = pg.transform.scale(wall_img_ig, (wall_img_ig.get_width() // 5, wall_img_ig.get_height() // 5))
elixir_img = pg.transform.scale(elixir_img, (elixir_img.get_width() // 5, elixir_img.get_height() // 5))
coin_img = pg.transform.scale(coin_img, (coin_img.get_width() // 10, coin_img.get_height() // 10))

resource_e_low_img = pg.transform.scale(resource_e_low_img, (resource_e_low_img.get_width() // 1.2, resource_e_low_img.get_height() // 1.2))
resource_e_mid_img = pg.transform.scale(resource_e_mid_img, (resource_e_mid_img.get_width() // 1.2, resource_e_mid_img.get_height() // 1.2))
resource_e_full_img = pg.transform.scale(resource_e_full_img, (resource_e_full_img.get_width() // 1.2, resource_e_full_img.get_height() // 1.2))
resource_g_low_img = pg.transform.scale(resource_g_low_img, (resource_g_low_img.get_width() // 1.2, resource_g_low_img.get_height() // 1.2))
resource_g_mid_img = pg.transform.scale(resource_g_mid_img, (resource_g_mid_img.get_width() // 1.2, resource_g_mid_img.get_height() // 1.2))
resource_g_full_img = pg.transform.scale(resource_g_full_img, (resource_g_full_img.get_width() // 1.2, resource_g_full_img.get_height() // 1.2))

# TODO TRANSLATE THE OTHER IMAGES

TILESIZE = WIDTH // 63

BGCOLOR = DARKGREY

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')