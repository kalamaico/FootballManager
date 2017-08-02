import unittest
from resources.match import *
from resources.random_generator import *
import resources.terrain

class TestMatch(unittest.TestCase):
    
    def setUp(self):
        self.team_a = ""
        self.team_b = ""
        self.rng = RandomGenerator()
        self.terrain = Terrain(5,5)
        self.match = Match(self.team_a, self.team_b, self.rng, self.terrain, 5)
        
        
    def test_generate_minutes(self):
        vals = self.match.generate_minutes()
        self.assertEqual(len(vals), 5)
        for i in range(0,5):
            self.assertTrue(vals[i] >= 1)
            self.assertTrue(vals[i] <= 90)
            
            
    def test_generate_starting_zones(self):
        vals = self.match.generate_starting_zones()
        self.assertEqual(len(vals), 5)
        for i in range(0,5):
            self.assertTrue(vals[i] >= 5)
            self.assertTrue(vals[i] <= 19)
            
            
    def test_generate_team_action(self):
        vals = self.match.generate_team_action('a')
        self.assertEqual(len(vals), 5)
        for i in range(0,5):
            self.assertTrue(vals[i][0] >= 1)
            self.assertTrue(vals[i][0] <= 90)
            self.assertTrue(vals[i][1] >= 0)
            self.assertTrue(vals[i][1] <= self.terrain.get_max_zone)
            self.assertTrue(vals[i][2] == 'a')
        
