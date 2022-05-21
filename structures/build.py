from config import *

class Build:
    def __init__(self, types):
        # self.rows = 64
        # self.col = 36
        self.box_size = WIDTH // 63
        self.type = types
        self.arr = []

    # Get the square that the mouse is over
    def get_pos(self):
        mouse = pg.mouse.get_pos()
        x = mouse[0]
        y = mouse[1]
        x = x // TILESIZE
        y = y // TILESIZE
        return (x, y)
    
    def draw(self):
        ix, iy = self.get_pos()
        # print(ix, iy)
        self.cx, self.cy = ix * TILESIZE, iy * TILESIZE
        # print(self.cx, self.cy, TILESIZE)

        
        if(self.type == 'CAN'):
            self.square = pg.Rect(self.cx, self.cy, TILESIZE*2, TILESIZE*2)
            if(self.is_on_point_can() != 0):
                pg.draw.rect(gameDisplay, (255,0,0), self.square)
                return
            pg.draw.rect(gameDisplay, (124,252,0), self.square)
            return
        if(self.type == 'WAL'):
            self.square = pg.Rect(self.cx, self.cy, TILESIZE, TILESIZE)
            if(self.is_on_point_wal() != 0):
                pg.draw.rect(gameDisplay, (255,0,0), self.square)
                return
            
            pg.draw.rect(gameDisplay, (124,252,0), self.square)
            return

    
    def draw_all(self, array = []):
        self.arr = array
        # print("X", self.arr[0][0])
        # print("Y", self.arr[0][1])
        # print("TYPE", self.arr[0][2])
        x, y = self.arr[0][0], self.arr[0][1]

        for i in range(0, len(self.arr)):
            if(self.arr[i][2] == 'CAN'):
                x, y = self.arr[i][0], self.arr[i][1]
                gameDisplay.blit(cannon_img_ig, (x * TILESIZE, y * TILESIZE))
            else:
                x, y = self.arr[i][0], self.arr[i][1]
                gameDisplay.blit(wall_img_ig, (x * TILESIZE, y * TILESIZE))

    
    # Add item/s
    def add(self):

        x, y = self.get_pos()

        if(self.type == 'CAN'):
            if(self.is_on_point_can() != 0):
                # print(self.is_on_point_can())
                return -1
            # self.arr.append((x, y, 'CAN'))
            return (x, y, 'CAN')

        else:
            if(self.is_on_point_wal() != 0):
                # print(self.is_on_point_wal())
                return -1
            # self.arr.append((x, y, 'WAL'))
            return (x, y, 'WAL')
    
    def add_static(self, coords):
        x = coords[0]
        y = coords[1]
        if(self.type == 'CAN'):
            return (x, y, 'CAN')
        else:
            return (x, y, 'WAL')

    # FUNC that shows if your mouse is over an object
    def is_on_point_can(self):
        
        x, y = self.get_pos()
        
        for i in range(0, len(self.arr)):
            if(self.arr != []):
                # print(x, y)
                # print(self.arr[i][0])
                # print(self.arr[i][1])
                if(x == self.arr[i][0] and y == self.arr[i][1]):
                    # print("FIRST", x)
                    # print("SECOND", self.arr[i - 1][0])
                    return 1

                elif(x == self.arr[i][0] + 1 and y == self.arr[i][1]):   
                    return 2
                elif(x == self.arr[i][0] - 1 and y == self.arr[i][1]):   
                    return 2

                elif(y == self.arr[i][1] + 1 and x == self.arr[i][0]):   
                    return 2
                elif(y == self.arr[i][1] - 1 and x == self.arr[i][0]):   
                    return 2

                elif(x == self.arr[i][0] + 1 and y == self.arr[i][1] + 1):
                    return 2   
                elif(x == self.arr[i][0] - 1 and y == self.arr[i][1] - 1):
                    return 2 

                elif(y == self.arr[i][1] + 1 and x == self.arr[i][0] - 1):
                    return 2   
                elif(y == self.arr[i][1] - 1 and x == self.arr[i][0] + 1):
                    return 2 

            else:
                return 0

        return 0

    def is_on_point_wal(self):
        x, y = self.get_pos()
        
        for i in range(0, len(self.arr)):
            if(self.arr != []):

                if(self.arr[i][2] == 'CAN'):
                    if(x == self.arr[i][0] and y == self.arr[i][1]):
                        return 1
                    elif(x == self.arr[i][0] + 1 and y == self.arr[i][1]):   
                        return 2
                    elif(y == self.arr[i][1] + 1 and x == self.arr[i][0]):   
                        return 2
                    elif(y == self.arr[i][1] + 1 and x == self.arr[i][0] + 1):   
                        return 2

                    # elif(x == self.arr[i][0] + 1 and y == self.arr[i][1] + 1):
                    #     return 2   
                    # elif(x == self.arr[i][0] - 1 and y == self.arr[i][1] - 1):
                    #     return 2 

                    # elif(y == self.arr[i][1] + 1 and x == self.arr[i][0] - 1):
                    #     return 2   
                    # elif(y == self.arr[i][1] - 1 and x == self.arr[i][0] + 1):
                    #     return 2 
                else:
                # print(x, y)
                # print(self.arr[i][0])
                # print(self.arr[i][1])
                    if(x == self.arr[i][0] and y == self.arr[i][1]):
                        # print("FIRST", x)
                        # print("SECOND", self.arr[i - 1][0])
                        return 1
            else:
                return 0
        return 0
    # #check whether the mouse in in the grid
    # def In_grid(self,x,y):
    #     if 0 > x > self.col-1:
    #         return False
    #     if 0 > y > self.rows-1:
    #         return False
    #     return True