#!python

from resources.player import *

class Team:
	def __init__(self, players, positions):
		if len(players) != len(positions):
			raise ValueError("Player and position have different length")
		
		# build dictionary position:player
		self._data = dict()
		for k,v in zip(positions, players):
			self._data[k] = v
			
		
	def has_player_in_position(self, zone):
		return self._data.has_key(zone)
		
	def get_player_in_position(self, zone):
		if not self.has_player_in_position(zone):
			raise ValueError("Player not present in position " + str(zone))
		else:
			return self._data[zone]
			
	#def generate # to use in tests
	
	#def fixed #to use in tests
	
	#def chosen_player(zone):
		# pick player closer to given zone
		
	#def support(zone):
		# pick support player in given zone
