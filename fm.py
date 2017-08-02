#!python

import random, time
import decimal
from resources.player import *


# cap bonus to +/- 5
MAX_BONUS = 5 
MIN_BONUS = -5

BOTCH = -1000
FAIL = -100

## Utils, I will refactor later
def generate_random_skill(min_value=1, max_value=15):
	return round(decimal.Decimal(random.uniform(min_value, max_value)),2)
	
def roll(min_value=1, max_value=20):
	v = random.randint(min_value, max_value)
	print " - rolled " + str(v)
	return v
	
def test_skill(skill, roll):
	return skill - roll
		
def generate_keeper():
	return Goalkeeper(generate_random_skill(), generate_random_skill(), generate_random_skill() )
	
def generate_outfielder():
	return Outfielder(generate_random_skill(), generate_random_skill(), generate_random_skill(), 
		generate_random_skill(), generate_random_skill(), generate_random_skill(), generate_random_skill(), 
		generate_random_skill())
		
def cap_result(value):
	if value > MAX_BONUS:
		print "- capping " + str(value) + " to " + str(MAX_BONUS)
		return MAX_BONUS
	elif value < MIN_BONUS:
		print "- capping " + str(value) + " to " + str(MIN_BONUS)
		return MIN_BONUS
	else:
		return value

# Game actions
def resolve_action(attacker_skill, defender_skill, delta_physical, bonus=0, support=0):
	print "-- attacker skill " + str(attacker_skill)
	print "-- defender skill " + str(defender_skill)
	print "-- delta physical  " + str(delta_physical)
	print "-- bonus " + str(bonus)
	print "-- support " + str(support)
	
	attack_roll = roll()
	defence_roll = roll()
	
	attack = test_skill(attacker_skill, attack_roll) + delta_physical + bonus + support
	defence = test_skill(defender_skill, defence_roll)
	print "- Attack value: " + str(attack)
	print "- Defence value: " + str(defence)
	if attack_roll == 20: # attacker botches
		print "- Attacker botches"
		return BOTCH
	elif defence_roll == 20: #defender rolls 20, automatic success with max bonus
		print "- Defender rolled 20, automatic success with max bonus"
		return MAX_BONUS	
	elif attack_roll == 1 and defence_roll == 1: # both succeed, standard result
		print "- Both players rolled 1, standard comparison " + str(attack - defence)
		return cap_result(attack - defence)
	elif attack_roll == 1: # attacker rolls 1, double its score
		print "- Attacker rolled 1, automatic succeed with " + str(2 * attack - defence)
		return cap_result(2 * attack - defence)
	elif defence_roll == 1: #defender rolls 1, automatic fail
		print "- Defender rolled 1, automatic fail"
		return FAIL
	elif attack < 0: # attacker fails
		print "- Attacker fails with " + str(attack)
		return FAIL #don't cap, if < 0 it means failure
	elif defence < 0: # defender fails
		print "- Attacker succeeds with " + str(attack)
		return cap_result(attack)
	else: # both succeed, compute result
		print "- Attacker succeeds with " + str(attack - defence)
		return cap_result(attack - defence)
		
		

## MAIN ##
random.seed(time.clock())

#a = Goalkeeper(1,2,3)
#b = Outfielder(1,2,3,4,5,6,7,8)
#a.to_string()
#b.to_string()

#attacker = generate_outfielder()
#attacker.to_string()
attacker = Outfielder(7, 5, 4, 4, 10, 4, 10, 2)
print "---"
#defender = generate_outfielder()
#defender.to_string()
defender = Outfielder(7, 5, 10, 4, 4, 4, 4, 2)
print "---"
keeper = Goalkeeper(7, 5, 10)
#keeper.to_string()
print "==="
delta_physical = attacker._physical - defender._physical
print "Physical delta: " + str(delta_physical)
print "Pass 1"
v1 = resolve_action(attacker._passing, defender._defence, delta_physical)
print "Pass 2"
v2 = resolve_action(attacker._passing, defender._defence, delta_physical, v1)
print "Shoot"
v3 = resolve_action(attacker._shooting, keeper._keeper, delta_physical, v2)


