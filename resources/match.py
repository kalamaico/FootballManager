#!python

from resources.random_generator import *
from resources.terrain import *
import pdb

class Match:
    def __init__(self, team_a, team_b, rng, n_actions = 8):
        self._team_a = team_a
        self._team_b = team_b
        self.generator = rng
        self._n_actions = n_actions
        
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
        
    def generate_actions(self, n_actions, generator):
        actions_a = generate_team_action('a', self._n_actions, generator)
        actions_a = generate_team_action('b', self._n_actions, generator)
        # merge list
        # sort by minutes
        
    def generate_team_action(self, team, n_actions, generator):
        zones = generate_starting_zones(n_actions, terrain, generator)
        for i in zones:
            actions = (team, i)
        minutes = generate_minutes(n_actions, generator)
        return zip(actions, minutes)
        
    def generate_minutes(self, n_actions, generator):
        return generator.generate_int_sequence_no_repetitions(n_actions, 1, 90)
        
    def generate_starting_zones(self, n_actions, generator, terrain):
        midfield_row = terrain.get_midfield_row()
        width = terrain.get_width()
        max_zone = (midfield_row +1) * width + width -1
        min_zone = (midfield_row -1) * width
        return generator.generate_int_sequence_no_repetitions(n_actions, min_zone, max_zone)
        
    

