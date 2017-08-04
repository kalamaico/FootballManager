import unittest
from resources.terrain import *

class TestTerrain(unittest.TestCase):
    
    def setUp(self):
        self.terrain = Terrain(5,5)
        self.terrain2 = Terrain(5,7)

	# distance computation
    def test_distance(self):
        self.assertEqual(self.terrain.distance(1,22),5)
        self.assertEqual(self.terrain.distance(1,1),0)
        self.assertEqual(self.terrain.distance(1,11),2)
        self.assertEqual(self.terrain.distance(20,4),8)
        self.assertEqual(self.terrain.distance(5,9),4)
        
    # location of corners
    def test_corners(self):
		self.assertTrue(0 in self.terrain._corners)
		self.assertTrue(4 in self.terrain._corners)
		self.assertTrue(20 in self.terrain._corners)
		self.assertTrue(24 in self.terrain._corners)
		
	# location of sides
    def test_in_sides(self):
        self.assertTrue(self.terrain.in_sides(0))
        self.assertTrue(self.terrain.in_sides(4))
        self.assertTrue(self.terrain.in_sides(20))
        self.assertTrue(self.terrain.in_sides(24))
        self.assertTrue(self.terrain.in_sides(5))
        self.assertTrue(self.terrain.in_sides(19))
        self.assertFalse(self.terrain.in_sides(12))
        
    # location of defence
    def test_in_defence(self):
        self.assertTrue(self.terrain.in_defence(0))
        self.assertTrue(self.terrain.in_defence(1))
        self.assertTrue(self.terrain.in_defence(2))
        self.assertTrue(self.terrain.in_defence(3))
        self.assertTrue(self.terrain.in_defence(4))
        self.assertFalse(self.terrain.in_defence(8))
        
    # location of defensive midfield
    def test_in_defensive_midfield(self):
        self.assertFalse(self.terrain.in_defensive_midfield(4))
        self.assertTrue(self.terrain.in_defensive_midfield(5))
        self.assertTrue(self.terrain.in_defensive_midfield(6))
        self.assertTrue(self.terrain.in_defensive_midfield(7))
        self.assertTrue(self.terrain.in_defensive_midfield(8))
        self.assertTrue(self.terrain.in_defensive_midfield(9))
        self.assertFalse(self.terrain.in_defensive_midfield(10))
        
        self.assertFalse(self.terrain2.in_defensive_midfield(4))
        self.assertTrue(self.terrain2.in_defensive_midfield(5))
        self.assertTrue(self.terrain2.in_defensive_midfield(6))
        self.assertTrue(self.terrain2.in_defensive_midfield(7))
        self.assertTrue(self.terrain2.in_defensive_midfield(8))
        self.assertTrue(self.terrain2.in_defensive_midfield(9))
        self.assertTrue(self.terrain2.in_defensive_midfield(10))
        self.assertTrue(self.terrain2.in_defensive_midfield(11))
        self.assertTrue(self.terrain2.in_defensive_midfield(12))
        self.assertTrue(self.terrain2.in_defensive_midfield(13))
        self.assertTrue(self.terrain2.in_defensive_midfield(14))
        self.assertFalse(self.terrain2.in_defensive_midfield(15))
        
    # location of midfield
    def test_in_midfield(self):
        self.assertFalse(self.terrain.in_midfield(9))
        self.assertTrue(self.terrain.in_midfield(10))
        self.assertTrue(self.terrain.in_midfield(11))
        self.assertTrue(self.terrain.in_midfield(12))
        self.assertTrue(self.terrain.in_midfield(13))
        self.assertTrue(self.terrain.in_midfield(14))
        self.assertFalse(self.terrain.in_midfield(15))
        
    # location of attacking midfield
    def test_in_attacking_midfield(self):
        self.assertFalse(self.terrain.in_attacking_midfield(14))
        self.assertTrue(self.terrain.in_attacking_midfield(15))
        self.assertTrue(self.terrain.in_attacking_midfield(16))
        self.assertTrue(self.terrain.in_attacking_midfield(17))
        self.assertTrue(self.terrain.in_attacking_midfield(18))
        self.assertTrue(self.terrain.in_attacking_midfield(19))
        self.assertFalse(self.terrain.in_attacking_midfield(20))
        
        self.assertFalse(self.terrain2.in_attacking_midfield(19))
        self.assertTrue(self.terrain2.in_attacking_midfield(20))
        self.assertTrue(self.terrain2.in_attacking_midfield(21))
        self.assertTrue(self.terrain2.in_attacking_midfield(22))
        self.assertTrue(self.terrain2.in_attacking_midfield(23))
        self.assertTrue(self.terrain2.in_attacking_midfield(24))
        self.assertTrue(self.terrain2.in_attacking_midfield(25))
        self.assertTrue(self.terrain2.in_attacking_midfield(26))
        self.assertTrue(self.terrain2.in_attacking_midfield(27))
        self.assertTrue(self.terrain2.in_attacking_midfield(28))
        self.assertTrue(self.terrain2.in_attacking_midfield(29))
        self.assertFalse(self.terrain2.in_attacking_midfield(30)) 
    
    # location of attack    
    def test_in_attack(self):
        self.assertFalse(self.terrain.in_attack(19))
        self.assertTrue(self.terrain.in_attack(20))
        self.assertTrue(self.terrain.in_attack(21))
        self.assertTrue(self.terrain.in_attack(22))
        self.assertTrue(self.terrain.in_attack(23))
        self.assertTrue(self.terrain.in_attack(24))
		
	# support zones for corners
    def test_get_support_ahead_behind_corner(self):
		self.assertEqual(self.terrain.get_support_ahead_behind_corner(0), [5,6,10])
		self.assertEqual(self.terrain.get_support_ahead_behind_corner(4), [8,9,14])
		self.assertEqual(self.terrain.get_support_ahead_behind_corner(20), [10,15,16])
		self.assertEqual(self.terrain.get_support_ahead_behind_corner(24), [14,18,19])
		with self.assertRaises(ValueError):
			self.terrain.get_support_ahead_behind_corner(13)
			
	# support zones for row ahead (corners excluded)
    def test_get_support_ahead(self):
		self.assertEqual(self.terrain.get_support_ahead(6), [10,11,12])
		self.assertEqual(self.terrain.get_support_ahead(12), [16,17,18])
		self.assertEqual(self.terrain.get_support_ahead(3), [7,8,9])
		self.assertEqual(self.terrain.get_support_ahead(9), [13,14,19])
		self.assertEqual(self.terrain.get_support_ahead(15), [20,21])
		with self.assertRaises(ValueError):
			self.terrain.get_support_ahead(21)
		with self.assertRaises(ValueError):
			self.terrain.get_support_ahead(22)
			
	# support zones for row behind (corners excluded)
    def test_get_support_behind(self):
		self.assertEqual(self.terrain.get_support_behind(16), [10,11,12])
		self.assertEqual(self.terrain.get_support_behind(12), [6,7,8])
		self.assertEqual(self.terrain.get_support_behind(18), [12,13,14])
		self.assertEqual(self.terrain.get_support_behind(9), [3,4])
		self.assertEqual(self.terrain.get_support_behind(15), [5,10,11])
		with self.assertRaises(ValueError):
			self.terrain.get_support_behind(0)
		with self.assertRaises(ValueError):
			self.terrain.get_support_behind(2)	
	
	# support zones for the same line
    def test_get_support_line(self):
		self.assertEqual(self.terrain.get_support_line(1), [0,2,3,4])		
        
    # support zones complete computation
    def test_get_support_area(self):
		self.assertEqual(self.terrain.get_support_area(12), [6,7,8,10,11,13,14,16,17,18])
		self.assertEqual(self.terrain.get_support_area(20), [10, 15, 16, 21, 22, 23, 24])
		self.assertEqual(self.terrain.get_support_area(9), [3,4,5,6,7,8,13,14,19])
		self.assertEqual(self.terrain.get_support_area(1), [0,2,3,4,5,6,7])
		self.assertEqual(self.terrain.get_support_area(21), [15,16,17,20,22,23,24])
        
    def test_get_midfield_row(self):
        self.assertEqual(self.terrain.get_midfield_row(), 2)
        self.assertEqual(self.terrain2.get_midfield_row(), 3)
        
    def test_get_defence_zone(self):
        self.assertEqual(self.terrain.get_defence_zone(0), 24)
        self.assertEqual(self.terrain.get_defence_zone(24), 0)
        self.assertEqual(self.terrain.get_defence_zone(9), 15)
        
    def test_get_max_zone(self):
        self.assertEqual(self.terrain.get_max_zone(), 24)
        self.assertEqual(self.terrain2.get_max_zone(), 34)

if __name__ == '__main__':
    unittest.main()
