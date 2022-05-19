from config import *

class Map():
    def __init__(self, arr):
        self.arr = arr

    def getBuildings(self):
        for item in self.arr:
            if(item != '0'):
                print("a")
    