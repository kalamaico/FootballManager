import unittest
from resources.team import *
from resources.player import *

class TestTeam(unittest.TestCase):

	# test constructor
    def test_constructor(self):
        player = Outfielder(7, 5, 10, 4, 4, 4, 4, 2)
        players = [player, player]
        positions = [1,2]
        team = Team(players, positions)
        self.assertTrue(team.has_player_in_position(1))
        self.assertTrue(team.has_player_in_position(2))
        self.assertFalse(team.has_player_in_position(3))
        self.assertTrue(team.get_player_in_position(2) == player)
        with self.assertRaises(ValueError):
			team.get_player_in_position(5)
        with self.assertRaises(ValueError):
			team2 = Team(players, [1])
