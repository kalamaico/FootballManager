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
        self.match = Match(self.team_a, self.team_b, self.rng)
        
        
    def test_generate_minutes(self):
        vals = self.match.generate_minutes(5, self.rng)
        self.assertEqual(len(vals), 5)
        for i in range(0,5):
            self.assertTrue(vals[i] >= 1)
            self.assertTrue(vals[i] <= 90)
            
    
    def test_generate_starting_zones(self):
        vals = self.match.generate_starting_zones(5, self.rng, self.terrain)
        self.assertEqual(len(vals), 5)
        for i in range(0,5):
            self.assertTrue(vals[i] >= 5)
            self.assertTrue(vals[i] <= 19)
