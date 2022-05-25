from config import *
# from structures.input import InputBox
# from structures.label import Label
# from structures.label import DynLabel These don't return
# from structures.buttons import Buttons
# from structures.buttons import Button
# from structures.level import Level
from structures.build import Build
from structures.overlay import Resources
from structures.player import Player
from structures.costs import *
from structures.menus import *
from structures.save import *
from structures.arcmatrix import *
from libs.pathfinding import Pathfinder
import unittest

testobj_build = Build('CAN')
testobj_resources = Resources(100, 'ELI')
testobj_player = Player(123123)
testobj_pathfinder = Pathfinder(create_empty_matrix())
testobj_hero = testobj_pathfinder.Hero.sprite

class TestStringMethods(unittest.TestCase):

    # BUILD GET POSITION
    def test_build_get_pos(self):
        self.assertEqual(testobj_build.get_pos(), (pg.mouse.get_pos()[0]//TILESIZE, pg.mouse.get_pos()[1]//TILESIZE))

    def test_build_draw(self):
        self.assertIsNone(testobj_build.draw())

    # EMPTY ARRAY
    def test_build_drawall(self):
        self.assertFalse(testobj_build.draw_all())
    
    def test_build_add(self):
        self.assertIsNotNone(testobj_build.add())

    def test_build_add_static(self):
        coords = (5, 10)
        func = testobj_build.add_static(coords)
        self.assertEqual((func[0], func[1]), coords)
    

    # RESOURSES
    def test_resources_get_money(self):
        self.assertEqual(testobj_resources.get_credits(), 100)

    def test_resources_remove_money(self):
        credits = testobj_resources.get_credits() - 50
        testobj_resources.remove_monez(50)
        self.assertEqual(credits, testobj_resources.get_credits())

    def test_resources_repr(self):
        self.assertEqual('50', str(testobj_resources))


    # PLAYER
    def test_player_repr(self):
        self.assertEqual('123123', str(testobj_player))
    

    # COSTS
    def test_buycannon_True(self):
        self.assertTrue(buy_cannon(3000))

    def test_buycannon_False(self):
        self.assertFalse(buy_cannon(30))

    def test_buywall_True(self):
        self.assertTrue(buy_wall(500))

    def test_buywall_False(self):
        self.assertFalse(buy_wall(50))
    

    # MENUS
    def test_menus_False(self):
        self.assertFalse(exited(False))


    # MATRIX
    def test_matrixes(self):
        matrix = create_empty_matrix()
        arc = matrix_to_arc(matrix)
        matrix2 = arc_to_matrix(matrix, arc)
        self.assertEqual(matrix, matrix2)


    # PATHFINDER
    def test_pathfinder_tiles(self):
        self.assertEqual(testobj_pathfinder.get_tiles(), (100, 100)) # DEFAULTS
    
    def test_pathfinder_coords(self):
        self.assertEqual(testobj_pathfinder.hero_getpos(), (60, 60)) # DEFAULTS


    # HERO
    def test_hero_get_coord(self):
        self.assertEqual(testobj_hero.get_coord(), (3, 3)) # testobj_pathfinder.get_tiles() // TILESIZE

    def test_hero_get_pos(self):
        self.assertEqual(testobj_pathfinder.hero_getpos(), testobj_hero.get_pos())
    

if __name__ == '__main__':
    unittest.main()