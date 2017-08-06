import unittest
from resources.match import *
from resources.random_generator import *
from resources.team import *
from resources.player import *
import resources.terrain

class TestMatch(unittest.TestCase):
    
    def setUp(self):
        self._terrain = Terrain(7,7)
        self._player1 = Outfielder("player1", 7, 5, 10, 4, 4, 4, 4, 2)
        self._player2 = Outfielder("player2", 7, 5, 10, 4, 4, 4, 4, 2)
        self._player3 = Outfielder("player3", 7, 5, 10, 4, 4, 4, 4, 2)
        self._player4 = Outfielder("player4", 7, 5, 10, 4, 4, 4, 4, 2)
        positions_a = [0, 3, 21, 23]
        positions_b = [23, 25, 39, 45]
        self._players_a = [self._player1, self._player2, self._player3, self._player4]
        self._team_a = Team(self._players_a, positions_a, self._terrain)
        self._players_b = [self._player1, self._player2, self._player3, self._player4]
        self._team_b = Team(self._players_b, positions_b, self._terrain)
        self._rng = RandomGenerator()
        self._terrain = Terrain(7,7)
        self._match = Match(self._team_a, self._team_b, self._rng, self._terrain, 5)
        
        
    def test_generate_minutes(self):
        vals = self._match.generate_minutes()
        self.assertEqual(len(vals), 5)
        for i in range(0,5):
            self.assertTrue(vals[i] >= 1)
            self.assertTrue(vals[i] <= 90)
            
            
    def test_generate_starting_zones(self):
        vals = self._match.generate_starting_zones()
        self.assertEqual(len(vals), 5)
        for i in range(0,5):
            self.assertTrue(vals[i] >= 0)
            self.assertTrue(vals[i] <= 27)
            
            
    def test_generate_team_action(self):
        vals = self._match.generate_team_action('a')
        self.assertEqual(len(vals), 5)
        for i in range(0,5):
            self.assertTrue(vals[i][0] >= 1)
            self.assertTrue(vals[i][0] <= 90)
            self.assertTrue(vals[i][1] >= 0)
            self.assertTrue(vals[i][1] <= 27)
            self.assertTrue(vals[i][2] == 'a')
            
    def test_generate_actions(self):
        vals = self._match.generate_actions()
        self.assertEqual(len(vals), 10)
        previous_minute = 0
        for i in range(0,10):
            self.assertTrue(vals[i][0] >= previous_minute)
            previous_minute = vals[i][0]
            self.assertTrue(vals[i][1] >= 0)
            self.assertTrue(vals[i][1] <= 27)
            self.assertTrue(vals[i][2] == 'a' or vals[i][2] == 'b')
        
    def test_get_support(self):
        zone = 8
        player = self._players_a[1]
        team = self._team_a
        self.assertEqual(self._match.get_support(zone, player, team), 1)
        
        zone = 40
        player = self._players_b[2]
        team = self._team_b
        self.assertEqual(self._match.get_support(zone, player, team), 0)
        
        zone = 3
        player = self._players_a[1]
        team = self._team_a
        self.assertEqual(self._match.get_support(zone, player, team), 1)
        
        zone = 45
        player = self._players_b[3]
        team = self._team_b
        self.assertEqual(self._match.get_support(zone, player, team), 1)        
        
        
        
        
        
