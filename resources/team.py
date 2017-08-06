#!python

from resources.player import *

class Team:
	def __init__(self, players, positions, terrain):
		if len(players) != len(positions):
			raise ValueError("Player and position have different length")
			
		self._terrain = terrain
		
		# build dictionary position:player
		self._positions_players = dict()
		for k,v in zip(positions, players):
			self._positions_players[k] = v
			
		
	def has_player_in_position(self, zone):
		return self._positions_players.has_key(zone)
		
	def get_player_in_position(self, zone):
		if not self.has_player_in_position(zone):
			raise ValueError("Player not present in position " + str(zone))
		else:
			return self._positions_players[zone]
			
	#def generate # to use in tests
	
	#def fixed #to use in tests
	
	# pick player closer to given zone
	def pick_closest_player(self, zone):
		if self.has_player_in_position(zone):
			return self.get_player_in_position(zone)
		else:
			# build a list of <distance, player at that distance>
			distances = []
			for i in self._positions_players.keys():
				distances.append( (self._terrain.distance(i, zone), self._positions_players[i]) )
			
			# sort tuples by distance and take the correspondent player
			selected_player = min(sorted(distances, key = lambda i: i[0]))[1]
			return selected_player
			
		
		
	#def support(zone):
		# pick support player in given zone
