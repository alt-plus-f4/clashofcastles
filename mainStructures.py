from config import *
from structures.input import InputBox
from structures.label import Label
from structures.buttons import Buttons
from structures.level import Level
from structures.menus import *
from libs.pyvidplayer import Video
import time

# Buttons here for now
attack_button = Buttons(WIDTH // 16, HEIGHT // 1.5, attack_img, 0.5)
shop_button = Buttons(WIDTH // 1.2, HEIGHT // 1.5, shop_img, 0.6)
cannon_buy = Buttons(280, 230, cannon_img, 1)
wall_buy = Buttons(730, 230, cannon_img, 1)
buy_menu_text = Label(200, 75, "Buy BUILDINGS")

class Game:
    def start():
        gameExit = False
        vid = Video("C:\\Users\\Valentin\\Desktop\\Programmin\\PROJECT PY\\nodont.mp4")
        vid.set_size((WIDTH, HEIGHT))
        start_time = time.time()
        while not gameExit:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    vid.close()
                    Game.enter_tag()
                if event.type == pg.QUIT:
                    gameExit = True

            vid.draw(gameDisplay, (0, 0))
            pg.display.update()

            current_time = time.time()
            elapsed_time = current_time - start_time
            if int(elapsed_time) > 2:
                vid.close()
                Game.enter_tag()
    def enter_tag():
        gameExit = False
        logged = False

        label = Label(300, 200, "Input tag:")
        input_box = InputBox(300, 250, 200, 50)

        while not gameExit:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    gameExit = True

                if(input_box.handle_event(event) == 420):
                    Game.main_game()

                input_box.update()

                gameDisplay.fill((30, 30, 30))

                label.draw(gameDisplay)
                input_box.draw(gameDisplay)


            pg.display.update()

            Clock = pg.time.Clock()
            Clock.tick(30)
        if gameExit:    
            pg.quit()
            quit()
    def main_game():
        gameExit = False
        
        arr = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']]

        newLevel = Level(arr)
        newLevel.draw()
        shop_open = False

        while not gameExit:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    gameExit = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    if(exited(shop_open)):
                        shop_open = False
                        newLevel.draw()
                
            # Click Shop
            if(shop_button.draw()):
                shop_menu()
                shop_open = True
            # Click Attack
            if(attack_button.draw()):
                print("attac")

            # newLevel.draw() lAgging
            if(shop_button.is_hovered() or attack_button.is_hovered()):
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
            elif(shop_open == True):
                if(cannon_buy.is_hovered() or wall_buy.is_hovered()):
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                else:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
            else:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
            
            if(shop_open):
                shop_menu()

            # Canon buy
            if(shop_open == True):
                buy_menu_text.draw(gameDisplay)
                if(cannon_buy.draw()):
                    print("Buy cannon!")
                if(wall_buy.draw()):
                    print("Buy wall!")

            pg.display.update()
            Clock = pg.time.Clock()
            Clock.tick(30)  

        pg.quit()
        quit()

Game.main_game()