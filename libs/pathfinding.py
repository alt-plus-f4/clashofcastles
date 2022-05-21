from config import *
from structures.menus import in_grid
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

class Pathfinder:
	def __init__(self,matrix):

		# SETUP
		self.matrix = matrix
		self.grid = Grid(matrix = matrix)
		self.select_surf = pg.image.load('.\\assets\\crosshair.png').convert_alpha()
		self.select_surf = pg.transform.scale(self.select_surf, (self.select_surf.get_width() // 1.4, self.select_surf.get_height() // 1.4))
		self.Hero = pg.sprite.GroupSingle(Hero(self.empty_path))
		
		# pathfinding
		self.path = []

	def empty_path(self):
		self.path = []

	def draw_active_cell(self):
		mouse_pos = pg.mouse.get_pos()
		row =  mouse_pos[1] // TILESIZE
		col =  mouse_pos[0] // TILESIZE
		# print("ROW: ", row)
		# print("COL: ", col)
		current_cell_value = self.matrix[row][col]

		# print(current_cell_value)

		if current_cell_value == 1:
			if(in_grid(pg.mouse.get_pos())):
				# print(in_grid(pg.mouse.get_pos()))
				rect = pg.Rect((col * TILESIZE,row * TILESIZE),(TILESIZE,TILESIZE))
				gameDisplay.blit(self.select_surf,rect)
		else:
			self.wall_or_cannon(row, col)


	def create_path(self):

		# start
		start_x, start_y = self.Hero.sprite.get_coord()
		start = self.grid.node(start_x,start_y)

		# end
		mouse_pos = pg.mouse.get_pos()
		end_x,end_y =  mouse_pos[0] // TILESIZE, mouse_pos[1] // TILESIZE  
		end = self.grid.node(end_x,end_y) 

		# path
		finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
		self.path,_ = finder.find_path(start,end,self.grid)
		self.grid.cleanup()
		self.Hero.sprite.set_path(self.path)
	def draw_path(self):
		if self.path:
			points = []
			for point in self.path:
				x = (point[0] * TILESIZE) + 16
				y = (point[1] * TILESIZE) + 16
				points.append((x,y))
			# self.get_target()
			if len(points) > 1:
				pg.draw.lines(gameDisplay,'#4a4a4a',False,points,5)
	def wall_or_cannon(self, row, col):
		rect = pg.Rect((col * TILESIZE,row * TILESIZE),(TILESIZE * 2,TILESIZE * 2))
		gameDisplay.blit(select_cannnon_img, rect)

	# def get_target(self, buildings):
	# 	for item in buildings:
	# 		x = item[0] // TILESIZE
	# 		y = item[1] // TILESIZE

	# 		print(x, y)
	# 		if((x, y) == pg.mouse.get_pos()):
	# 			return True
	# 	return False

	# I thought it would be more fun to have it manual
	# def get_target_auto:
	# 	max = 0
	# 	max_index = 0
	# 	index = 0

	# 	start_x, start_y = self.Hero.sprite.get_coord()
	# 	start = self.grid.node(start_x,start_y)

	# 	for item in buildings:
	# 		x = item[0]
	# 		y = item[0]

	# 		end_x,end_y =  x // TILESIZE, y // TILESIZE  
	# 		end = self.grid.node(end_x,end_y) 

	# 		finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
	# 		self.path,_ = finder.find_path(start,end,self.grid)
	# 		self.grid.cleanup()

	# 		if (max < len(self.path)):
	# 			max = (len(self.path))
	# 			max_index = index
	# 		index +=1
	# 	print(max, max_index)
	
	
	def update(self):
		self.draw_active_cell()
		self.draw_path()

		# Hero updating and drawing
		self.Hero.update()
		self.Hero.draw(gameDisplay)
	
	def update_grid(self, matrix):
		self.matrix = matrix
		self.grid = Grid(matrix = matrix)

# HERO

class Hero(pg.sprite.Sprite):
	def __init__(self,empty_path):

		# basic
		super().__init__()
		self.image = pg.image.load('.\\assets\\Hero.png').convert_alpha()
		self.image = pg.transform.scale(self.image, (self.image.get_width() // 15, self.image.get_height() // 15))
		self.rect = self.image.get_rect(center = (60,60))

		# movement 
		self.pos = self.rect.center
		self.speed = 3
		self.direction = pg.math.Vector2(0,0)

		# path
		self.path = []
		self.collision_rects = []
		self.empty_path = empty_path

	def get_coord(self):
		col = self.rect.centerx // TILESIZE
		row = self.rect.centery // TILESIZE
		# print("COL:", col)
		# print("ROW:", row)
		return (col,row)

	def set_path(self,path):
		self.path = path
		self.create_collision_rects()
		self.get_direction()

	def create_collision_rects(self):
		if self.path:
			self.collision_rects = []
			for point in self.path:
				x = (point[0] * TILESIZE) + 16
				y = (point[1] * TILESIZE) + 16
				rect = pg.Rect((x - 2,y - 2),(4,4))
				self.collision_rects.append(rect)

	def get_direction(self):
		if self.collision_rects:
			start = pg.math.Vector2(self.pos)
			end = pg.math.Vector2(self.collision_rects[0].center)
			self.direction = (end - start).normalize()
		else:
			self.direction = pg.math.Vector2(0,0)
			self.path = []

	def check_collisions(self):
		if self.collision_rects:
			for rect in self.collision_rects:
				if rect.collidepoint(self.pos):
					del self.collision_rects[0]
					self.get_direction()
		else:
			self.empty_path()

	def update(self):
		self.pos += self.direction * self.speed
		self.check_collisions()
		self.rect.center = self.pos