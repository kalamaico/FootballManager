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
            self.assertTrue(vals[i] >= 0)
            self.assertTrue(vals[i] <= 14)
            
            
    def test_generate_team_action(self):
        vals = self.match.generate_team_action('a')
        self.assertEqual(len(vals), 5)
        for i in range(0,5):
            self.assertTrue(vals[i][0] >= 1)
            self.assertTrue(vals[i][0] <= 90)
            self.assertTrue(vals[i][1] >= 0)
            self.assertTrue(vals[i][1] <= 14)
            self.assertTrue(vals[i][2] == 'a')
            
    def test_generate_actions(self):
        vals = self.match.generate_actions()
        self.assertEqual(len(vals), 10)
        previous_minute = 0
        for i in range(0,10):
            self.assertTrue(vals[i][0] >= previous_minute)
            previous_minute = vals[i][0]
            self.assertTrue(vals[i][1] >= 0)
            self.assertTrue(vals[i][1] <= 14)
            self.assertTrue(vals[i][2] == 'a' or vals[i][2] == 'b')
        
