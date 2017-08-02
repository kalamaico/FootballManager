#!python

from resources.random_generator import *
from resources.terrain import *
import pdb
from itertools import repeat

class Match:
    def __init__(self, team_a, team_b, rng, terrain, n_actions = 8):
        self._team_a = team_a
        self._team_b = team_b
        self._generator = rng
        self._terrain = terrain
        self._n_actions = n_actions  #per team
        
	#def play(self):
		# generate actions
		## action: <team, starting zone>
		## output: <minute, action>
		
		# loop over actions
		## pick attacking and defending players
		## decide what he's going to try
		## compute supports
		## resolve action
		## if successful, go to new zone and repeat, until failure or goal 
        
    def generate_actions(self):
        actions_a = self.generate_team_action('a')
        actions_a = self.generate_team_action('b')
        # merge list
        # sort by minutes
        
    def generate_team_action(self, team):
        zones = self.generate_starting_zones()
        minutes = self.generate_minutes()
        team = list(repeat(team, self._n_actions))
        
        return zip(minutes, zones, team)

        
    def generate_minutes(self):
        return self._generator.generate_int_sequence_no_repetitions(self._n_actions, 1, 90)
        
    def generate_starting_zones(self):
        midfield_row = self._terrain.get_midfield_row()
        width = self._terrain.get_width()
        max_zone = (midfield_row +1) * width + width -1
        min_zone = (midfield_row -1) * width
        return self._generator.generate_int_sequence(self._n_actions, min_zone, max_zone)
        
    

