from config import *
from structures.input import InputBox
from structures.label import Label
from structures.label import DynLabel
from structures.buttons import Buttons
from structures.level import Level
from structures.build import Build
from structures.overlay import Resources
from structures.costs import *
from structures.menus import *
from libs.pyvidplayer import Video
import time

# Buttons here for now
attack_button = Buttons(WIDTH // 16, HEIGHT // 1.5, attack_img, 0.5)
shop_button = Buttons(WIDTH // 1.2, HEIGHT // 1.5, shop_img, 0.6)
cannon_buy = Buttons(280, 230, cannon_img, 1)
cannon_text = Label(350, 510, "Cannon")
wall_buy = Buttons(730, 230, wall_img, 1)
wall_text = Label(835, 510, "Wall")
buy_menu_text = Label(200, 75, "Buy BUILDINGS")
x = Label(1108, 38, "X")

# Resources
gold = Resources(5000, 'GOL')
elixir = Resources(1000, 'ELI')

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
            ['0','0','0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']]

        newLevel = Level(arr)
        newLevel.draw()
        shop_open = False
        build = False
        selected = None
        more = False

        # architectures = PleaseHelp()

        architectures = []

        while not gameExit:

            # With some optimising it is fine to redraw everything 
            # just to have that semi-transparent buttons

            newLevel.draw()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    gameExit = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    if(exited(shop_open)):
                        shop_open = False
                        newLevel.draw()
                    if(build):

                        # RIGHT CLICK exits the menu

                        if(event.button == 3):
                            build = False
                            break
                        if(buildings.add() != -1):
                            architectures.append(buildings.add())
                            selected = 42
                            build = False
                            if(more):
                                gold.remove_monez(1000)
                            else:
                                elixir.remove_monez(500)
                        else:
                            print("hitormissiguesstheynevermisshuh?")
            
            if(not build):

                # Click Shop

                if(shop_button.draw()):
                    shop_menu()
                    shop_open = True

                # Click Attack

                if(attack_button.draw()):
                    attack_menu()
                    shop_open = True

                # Drawing resources bars and stuff

                gold.draw()
                elixir.draw()

            else:
                buildings.draw()

            if(selected != None):
                buildings.draw_all(architectures)

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
                cannon_text.draw(gameDisplay)
                wall_text.draw(gameDisplay)
                DynLabel(370, 200, (252, 242, 58), False, "1000")
                DynLabel(830, 200, (54, 11, 73), False, "500")

                x.draw(gameDisplay)

                if(cannon_buy.draw()):
                    if(buy_cannon(gold.get_credits())):
                        shop_open = False
                        build = True

                        # Buy cannon

                        buildings = Build('CAN')
                       
                        more = True
                        newLevel.draw()
                    # else:
                        # If I want to display a message
                        # print("no $")
                    
                if(wall_buy.draw()):
                    if(buy_wall(elixir.get_credits())):
                        shop_open = False
                        build = True

                        # Buy wall
                    
                        buildings = Build('WAL')
                        
                        more = False
                        newLevel.draw()
                    # else:
                        # If I want to display a message
                        # print("no $")

            pg.display.update()
            Clock = pg.time.Clock()
            Clock.tick(30)  

        pg.quit()
        quit()

Game.main_game()