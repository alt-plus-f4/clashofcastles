from config import *
from structures.input import InputBox
from structures.label import Label
from structures.label import DynLabel
from structures.buttons import Buttons
from structures.buttons import Button
from structures.level import Level
from structures.build import Build
from structures.overlay import Resources
from structures.player import Player
from structures.costs import *
from structures.menus import *
from structures.save import *
from structures.arcmatrix import *
from libs.pyvidplayer import Video
from libs.pathfinding import Pathfinder, Projectile
from random import randint
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
attack_start = Button(480, 300, attack_start_img)

class Game:
	def start():		
		gameExit = False

		vid = Video("assets\\nodont.mp4")
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

		pg.quit()
		quit()	
	def enter_tag():
		with open("tag.txt", "r") as f:
			tag = f.read()
			if(tag != ""):
				Game.main_game(tag)
			else:
				pass

		gameExit = False

		label = Label(550, 250, "Input tag:")
		input_box = InputBox(550, 300, 300, 50)


		while not gameExit:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					gameExit = True
				
				tag = input_box.handle_event(event)

				if(tag != None):

					# Current Player tag and stuff that I need which is only tag
					current_player_tag = Player(str(tag))

					Game.main_game(current_player_tag)

				input_box.update()

				gameDisplay.fill((30, 30, 30))

				label.draw(gameDisplay)
				input_box.draw(gameDisplay)


			pg.display.update()

			Clock = pg.time.Clock()
			Clock.tick(30) 
	   
		pg.quit()
		quit()
		
	def main_game(current_player_tag):
		mixer.music.load('assets\\soundtrack.mp3')
		mixer.music.play(-1)

		gameExit = False

		# MATRIX is here
		matrix, count_g, count_e = load(current_player_tag)
		
		# print("Load matrix ",matrix)

		matrix = stringtolist(matrix)

		# print("First matrix ",matrix[1][1])

		architectures = matrix_to_arc(matrix)
		if(architectures):
			buildings = Build('WAL')
			selected = 42
		else:
			selected = None

		# print("Arc", architectures , "\n")

		# Resources
		gold = Resources(count_g, 'GOL')
		elixir = Resources(count_e, 'ELI')

		# Pathfinder
		pathfinder = Pathfinder(matrix)

		newLevel = Level(matrix)
		newLevel.draw()
		dead = False
		shop_open = False
		build = False
		more = False
		is_open_attack = False
		attack = False
		startup = False

		# architectures = PleaseHelp()

		while not gameExit:
			if(dead):
				time.sleep(0.5)
				mixer.music.load('assets\\soundtrack.mp3')
				mixer.music.play(-1)

				matrix, count_g, count_e = load(current_player_tag)

				matrix = stringtolist(matrix)

				architectures = matrix_to_arc(matrix)
				if(architectures):
					buildings = Build('WAL')
					selected = 42
				else:
					selected = None

				newLevel = Level(matrix)
				newLevel.draw()
				shop_open = False
				build = False
				more = False
				is_open_attack = False
				attack = False
				startup = False

				dead = False

			# With some optimising it is fine to redraw everything 
			# just to have that semi-transparent buttons

			newLevel.draw()

			for event in pg.event.get():
				if event.type == pg.QUIT:
					# db.cursor.close()
					with open("tag.txt", "w") as f:
						f.write(str(current_player_tag))
					matrix = arc_to_matrix(matrix, architectures)
					# print("Matrix save", matrix[1][1])
					save(matrix, gold, elixir, current_player_tag)
					gameExit = True
				# Normal mode
				if(not attack):
					if event.type == pg.MOUSEBUTTONDOWN:
						if(exited(shop_open)):
							shop_open = False
							newLevel.draw()
						if(exited(is_open_attack)):
							is_open_attack = False
							newLevel.draw()
						if(build):

							# RIGHT CLICK exits the menu

							if(event.button == 3):
								build = False
								break

							#* If I want to have some kind of warning 
							# else:
							#     print("hitormissiguesstheynevermisshuh?")

							if(buildings.add() != -1):
								architectures.append(buildings.add())
								selected = 42
								build = False
								if(more):
									gold.remove_monez(1000)
								else:
									gold.remove_monez(100)		
				# Attack mode
				else:
					if event.type == pg.MOUSEBUTTONDOWN:
						# If mouse isn't in grid there is some kind of error idk why
						# SO add a check just to be sure
						position = pg.mouse.get_pos()
						pathfinder.create_path()
						# print("E")
					# if event.type == pg.KEYDOWN:
					# 	if(event.key == pg.K_SPACE):
					# 		print("a")
					# 		bullet = Projectile(info[0], info[1], 6, (0,0,0), info[2])
					# 		bullet.draw()

			# Normal mode
			if(not attack):
				if(not build):

					# Click Shop

					if(shop_button.draw()):
						shop_menu()
						shop_open = True

					# Click Attack

					if(attack_button.draw()):
						attack_menu()
						is_open_attack = True

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
				elif(is_open_attack):
					if(attack_start.is_hovered()):
						pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
						
					else:
						pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
				else:
					pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
				if(shop_open):
					shop_menu()
				if(is_open_attack):
					attack_menu()

				# Canon buy
				
				if(shop_open == True):

					buy_menu_text.draw(gameDisplay)
					cannon_text.draw(gameDisplay)
					wall_text.draw(gameDisplay)
					DynLabel(370, 200, GOLD_CR, False, "1000")
					DynLabel(830, 200, GOLD_CR, False, "100")

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
							#* If I want to display a message
							# print("no $")
						
					if(wall_buy.draw()):
						if(buy_wall(gold.get_credits())):
							shop_open = False
							build = True

							# Buy wall
						
							buildings = Build('WAL')
							
							more = False
							newLevel.draw()
						# else:
							#* If I want to display a message
							# print("no $")

				if(is_open_attack):
					DynLabel(500, 450, (0,0,0), 'big', "COST:")
					DynLabel(450, 200, red, True, "Don't get too close to the cannons or you'll see!")
					DynLabel(470, 220, red, True, "Also don't stay in the same place for a long time!")
					DynLabel(680, 450, ELIXIR_CR, 'big', "500")
					x.draw(gameDisplay)
					if(attack_start.draw()):
						attack = True
						elixir.remove_monez(500)
						architectures = []
						pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
			
			# Attacking
			else:
				if(startup == False):
					pathfinder = Pathfinder(matrix)
					
					mixer.music.load('assets\\soundtrack-attack.mp3')
					mixer.music.play(-1)
					position1 = None
					position = None
					attack_arc = []
					bullet = None
					wait = 0
					dead = False

					attack_matrix = init_attack_matrix()

					buildings_attack = Build('CANA')

					attack_arc = matrix_to_arc(attack_matrix, True)

					pathfinder.update_grid(attack_matrix)

					# print(pathfinder.matrix)
					
					startup = True
					# print(attack_arc)
				if(position != None):
					position1 = (round(position[0], -2), round(position[1], -2))

				newLevel.draw()
				buildings_attack.draw_all(attack_arc, pathfinder.hero_getpos())

				if((pathfinder.get_tiles() == position1) or position1 == None):
					wait+=1
				else:
					wait = 0

				# print(pathfinder.hero_getpos()[1])
				# print(wait)

				if((pathfinder.hero_getpos()[0] > 500 and pathfinder.hero_getpos()[0] < 800) and (pathfinder.hero_getpos()[1] > 150 and pathfinder.hero_getpos()[1] < 400)):
					mixer.init()
					mixer.music.load("assets\\shot.mp3")
					mixer.music.set_volume(1)
					mixer.music.play()

					dead = True
					attack = False

				# YOU LOSE
				if(wait > 15):
					mixer.init()
					mixer.music.load("assets\\shot.mp3")
					mixer.music.set_volume(1)
					mixer.music.play()

					dead = True
					attack = False
				
				# YOU WIN
				if(pathfinder.get_tiles()[0] >= 1300):
					elixir.remove_monez(-2000)
					gold.remove_monez(-500)
					dead = True

				pathfinder.update()

				# if bullet != None:
				# 	if bullet.x < 1280 and bullet.x > 0:
				# 		bullet.x += bullet.vel
				# 		bullet.draw()
				# 	else:
				# 		bullet = None
				# print(pathfinder.hero_getpos())


			pg.display.update()
			Clock = pg.time.Clock()
			Clock.tick(30)  

		pg.quit()
		quit()

# row = []
# whole = []

# for i in range(0, 36):
# 	whole.append(row)
# 	row = []
# 	for j in range(0,64):
# 		row.append(1)

# for asd in whole:
# 	print(asd)

Game.start()