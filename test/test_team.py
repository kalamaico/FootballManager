import unittest
from resources.team import *
from resources.player import *
from resources.terrain import *

class TestTeam(unittest.TestCase):
    
    def setUp(self):
        self._terrain = Terrain(7,7)
        self._player1 = Outfielder("player1", 7, 5, 10, 4, 4, 4, 4, 2)
        self._player2 = Outfielder("player2", 7, 5, 10, 4, 4, 4, 4, 2)
        self._player3 = Outfielder("player3", 7, 5, 10, 4, 4, 4, 4, 2)
        self._player4 = Outfielder("player4", 7, 5, 10, 4, 4, 4, 4, 2)
        positions = [0, 3, 21, 23]
        self._players = [self._player1, self._player2, self._player3, self._player4]
        self._team = Team(self._players, positions, self._terrain)

	# test constructor
    def test_constructor(self):
        self.assertTrue(self._team.has_player_in_position(0))
        self.assertFalse(self._team.has_player_in_position(2))
        self.assertTrue(self._team.get_player_in_position(0) == self._player1)
        with self.assertRaises(ValueError):
			self._team.get_player_in_position(5)
        with self.assertRaises(ValueError):
			team2 = Team(self._players, [1], self._terrain)
            
            
    def test_pick_closest_player(self):
        zone1 = 0
        self.assertEqual(self._team.pick_closest_player(zone1), self._player1)
        
        zone2 = 1
        self.assertTrue(self._team.pick_closest_player(zone2) == self._player1)
        
        zone3 = 7
        self.assertEqual(self._team.pick_closest_player(zone3), self._player1)
        
        zone4 = 10
        self.assertEqual(self._team.pick_closest_player(zone4), self._player2)

        zone5 = 9
        self.assertEqual(self._team.pick_closest_player(zone1), self._player1 or self._team.pick_closest_player(zone2) == self._player2 or self._team.pick_closest_player(zone2) == self._player3)
     
