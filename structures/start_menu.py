from config import *

def start_menu():
    user_pick = False

    startButton = pg.draw.rect(gameDisplay, blue, [250,100,300,100])
    quitButton = pg.draw.rect(gameDisplay, blue, [250,350,300,100])

    textStart = pg.font.Font.render(font,'Start', 1, white)
    textQuit = pg.font.Font.render(font,'Quit', 1, white)
    # print(textStart,textQuit)
    pg.Surface.blit(gameDisplay, textStart, (400 - textStart.get_width() // 2, 150 - textStart.get_height()))
    pg.Surface.blit(gameDisplay, textQuit, (400 - textQuit.get_width() // 2, 400 - textQuit.get_height()))
    pg.display.update()

    while not user_pick:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            # Hover effect, huh? Shit on python, embrase css.
            if event.type == pg.MOUSEMOTION:
                mouse_position = pg.mouse.get_pos()
                if pg.Rect.collidepoint(startButton, mouse_position):
                    startButton = pg.draw.rect(gameDisplay, blue, [250,100,300,100])
                    pg.Surface.blit(gameDisplay, textStart, (400 - textStart.get_width() // 2, 150 - textStart.get_height() // 2))
                    pg.Surface.blit(gameDisplay, textQuit, (400 - textQuit.get_width() // 2, 400 - textQuit.get_height() // 2))
                    pg.display.update()
                elif pg.Rect.collidepoint(quitButton, mouse_position):
                    quitButton = pg.draw.rect(gameDisplay, blue, [250,350,300,100])
                    pg.Surface.blit(gameDisplay, textStart, (400 - textStart.get_width() // 2, 150 - textStart.get_height() // 2))
                    pg.Surface.blit(gameDisplay, textQuit, (400 - textQuit.get_width() // 2, 400 - textQuit.get_height() // 2))
                    pg.display.update()
                else:
                    startButton = pg.draw.rect(gameDisplay, green, [250,100,300,100])
                    quitButton = pg.draw.rect(gameDisplay, green, [250,350,300,100])
                    pg.Surface.blit(gameDisplay, textStart, (400 - textStart.get_width() // 2, 150 - textStart.get_height() // 2))
                    pg.Surface.blit(gameDisplay, textQuit, (400 - textQuit.get_width() // 2, 400 - textQuit.get_height() // 2))
                    pg.display.update()

            if event.type == pg.MOUSEBUTTONDOWN:
                clickPos = pg.mouse.get_pos()
                # print(clickPos)
                if pg.Rect.collidepoint(startButton, clickPos):
                    # print('Game Started')
                    return 420
                elif pg.Rect.collidepoint(quitButton,clickPos):
                    # print('Quit Game')
                    user_pick = True
                    pg.quit()
                    quit()