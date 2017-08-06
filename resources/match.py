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
		## output: <minute, zone, team>
		
		# loop over actions
		## pick attacking and defending players
		## decide what he's going to try
		## compute supports
		## resolve action
		## if successful, go to new zone and repeat, until failure or goal 
        
        
    def process_action(self, action):
        state = "construction"
        attack_zone = action[1]
        defence_zone = self._terrain.get_defence_zone(attack_zone)
        if action[2] == 'a':
            attacking_team = self._team_a
            defending_team = self._team_b
        else:
            attacking_team = team_b
            defending_team = self._team_a
        
        ## construction
        
        # select players
        attacking_player = attacking_team.pick_closest_player(attack_zone)
        defending_player = defending_team.pick_closest_player(defence_zone)
        
        # attacking player decides what to do
        # decision depends onzone and on player skill (if skill needed for action is one of the top 3 of the player, with weigth)
        
        # compute support for both teams
        # for now, just count how many players are in the support zone
        # later, factor in their relevant skills
        attacking_support= get_support(attack_zone, attacking_player, attacking_team)
        attacking_support= get_support(defence_zone, defending_player, defending_team)
        
        # resolve action
        
        ## refining
        
        #* finalizing
        
    
    def get_support(self, zone, player, team):
        support_zones = self._terrain.get_support_area(zone)
        support = 0
        for i in support_zones:
            if team.has_player_in_position(i) and team.get_player_in_position(i) != player:
                support = support + 1
                
        return support
        
        
    #action is a tuple <minute, zone, team>
    def get_action_minute(self, action):
        return action[0]
        
    def generate_actions(self):
        # generate actions
        actions_a = self.generate_team_action('a')
        actions_b = self.generate_team_action('b')
        
        # merge list
        actions = actions_a + actions_b
        
        # sort by minutes
        return sorted(actions, key=self.get_action_minute)
        
        
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
        max_zone = midfield_row * width + width -1
        min_zone = 0
        return self._generator.generate_int_sequence(self._n_actions, min_zone, max_zone)
        
    

