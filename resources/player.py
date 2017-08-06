#!python

from resources.random_generator import *

class Player:
    def __init__(self, name, physical, mental):
        self._name = name
        self._physical = physical
        self._mental = mental
        
    def to_string(self):
        print "Name: " + self._name
        print "Physical: " + str(self._physical)
        print "Mental: " + str(self._mental)
        
    @classmethod
    def generate(cls, rng, level):
        if level > 10:
            raise ValueError("Level cannot be > 10")
        minval = level
        maxval = level + 4
        return Player(Player.generate_name(), rng.generate_int(minval,maxval), rng.generate_int(minval,maxval) )
    
    @classmethod
    def generate_name(cls):
        return "default"
    
class Goalkeeper(Player):
    def __init__(self, name, physical, mental, keeper):
        Player.__init__(self, name, physical, mental)
        self._keeper = keeper
        
    def to_string(self):
        Player.to_string(self)
        print "Keeper: " + str(self._keeper)
        
    @classmethod
    def generate(cls, rng, level):
        p = Player.generate(rng, level)
        minval = level + 1
        maxval = level + 3
        return Goalkeeper(p._name, p._physical, p._mental, rng.generate_int(minval,maxval))
        
        
class Outfielder(Player):
    def __init__(self, name, physical, mental, defence, cross, passing, dribbling, shooting, set_pieces):
        Player.__init__(self, name, physical, mental)
        self._defence = defence
        self._cross = cross
        self._passing = passing
        self._dribbling = dribbling
        self._shooting = shooting
        self._set_pieces = set_pieces
        
    def to_string(self):
        Player.to_string(self)
        print "Defence: " + str(self._defence)
        print "Cross: " + str(self._cross)
        print "Passing: " + str(self._passing)
        print "Dribbling: " + str(self._dribbling)
        print "Shooting: " + str(self._shooting)
        print "Set Pieces: " + str(self._set_pieces)
        
    @classmethod
    def generate(cls, rng, level, role):
        p = Player.generate(rng, level)
        mainskill_minval = level + 1
        mainskill_maxval = level + 3
        secondaryskill_minval = 1
        secondaryskill_maxval = 1 + level
        otherskill_minval = 1
        otherskill_maxval = 1 + level/2
        sp_minval = 1
        sp_maxval = 10
        if role == "central_defender":
            return Outfielder(p._name, p._physical, p._mental, \
                rng.generate_int(mainskill_minval, mainskill_maxval),\
                rng.generate_int(otherskill_minval, otherskill_maxval),\
                rng.generate_int(secondaryskill_minval, secondaryskill_maxval),\
                rng.generate_int(otherskill_minval, otherskill_maxval),\
                rng.generate_int(otherskill_minval, otherskill_maxval),\
                rng.generate_int(sp_minval, sp_maxval))
        elif role == "side_defender":
            return Outfielder(p._name, p._physical, p._mental, \
                rng.generate_int(mainskill_minval, mainskill_maxval),\
                rng.generate_int(secondaryskill_minval, secondaryskill_maxval),\
                rng.generate_int(otherskill_minval, otherskill_maxval),\
                rng.generate_int(otherskill_minval, otherskill_maxval),\
                rng.generate_int(otherskill_minval, otherskill_maxval),\
                rng.generate_int(sp_minval, sp_maxval))
        elif role == "midfielder":
            return Outfielder(p._name, p._physical, p._mental, \
                rng.generate_int(secondaryskill_minval, secondaryskill_maxval),\
                rng.generate_int(otherskill_minval, otherskill_maxval),\
                rng.generate_int(mainskill_minval, mainskill_maxval),\
                rng.generate_int(otherskill_minval, otherskill_maxval),\
                rng.generate_int(otherskill_minval, otherskill_maxval),\
                rng.generate_int(sp_minval, sp_maxval))
        elif role == "winger":
            return Outfielder(p._name, p._physical, p._mental, \
                rng.generate_int(otherskill_minval, otherskill_maxval),\
                rng.generate_int(mainskill_minval, mainskill_maxval), \
                rng.generate_int(otherskill_minval, otherskill_maxval),\
                rng.generate_int(secondaryskill_minval, secondaryskill_maxval), \
                rng.generate_int(otherskill_minval, otherskill_maxval),\
                rng.generate_int(sp_minval, sp_maxval))
        elif role == "attacker":
            return Outfielder(p._name, p._physical, p._mental, \
                rng.generate_int(otherskill_minval, otherskill_maxval),\
                rng.generate_int(otherskill_minval, otherskill_maxval),\
                rng.generate_int(otherskill_minval, otherskill_maxval),\
                rng.generate_int(secondaryskill_minval, secondaryskill_maxval),\
                rng.generate_int(mainskill_minval, mainskill_maxval),\
                rng.generate_int(sp_minval, sp_maxval))
