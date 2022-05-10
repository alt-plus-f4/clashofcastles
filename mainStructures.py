from config import *
from structures.input import InputBox
from structures.label import Label
from structures.buttons import Buttons
from structures.level import Level
from libs.pyvidplayer import Video
import time

# Buttons here for now
attack_button = Buttons(WIDTH // 16, HEIGHT // 1.5, attack_img, 0.5)
shop_button = Buttons(WIDTH // 1.2, HEIGHT // 1.5, shop_img, 0.6)

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
        arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        newLevel = Level(arr)
        newLevel.draw()

        while not gameExit:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    gameExit = True
                # if(newLevel.handle_event(event) == 420):
                newLevel.handle_event(event)
                    # Game.main_game()
            
            # Click Shop
            if(shop_button.draw()):
                print("shop")

            # Click Attack
            if(attack_button.draw()):
                print("attac")

            if(shop_button.is_hovered() or attack_button.is_hovered()):
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)

            else:
                pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

            pg.display.update()
            Clock = pg.time.Clock()
            Clock.tick(30)  

        pg.quit()
        quit()

Game.main_game()