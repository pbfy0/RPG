import pprint
import core, races, classes, enemies, moves
import random
p = pprint.PrettyPrinter().pprint

unlocked = dict(gladiator=False, sage=False, saint=False, joker=False, master=False)
def choose_race():
	race = input('Race: ')
	while not race in races.races:
		race = input('  ... ').lower()
	return races.races[race]
def choose_class():
	class_ = input('Class: ').lower()
	while not class_ in classes.classes:
		class_ = input('   ... ').lower()
	return classes.classes[class_]

name = input('Name: ')
race = choose_race()
class_ = choose_class()
player_type = type('Player', (core.Player, race, class_), {})
player = player_type(race, class_, name)
for i in player.moves: print(i.desc())
#p(x.__dict__)
while True:
	enemy_choices, dl = [], 2
	while len(enemy_choices) == 0:
		enemy_choices = [x for x in enemies.enemies if abs(player.level - x.level) < dl]
		dl += 1
	enemy = random.choice(enemy_choices)
	ce = enemy()
	print('A {enemy} has spotted you!'.format(enemy=str(ce)))
	ps, es = (x*random.random()/4+0.875 for x in (player.stats['speed'], ce.stats['speed']))
	attacker, attacked = (player, ce) if ps > es else (ce, player)
	while True:
		attacker.every_round()
		move = attacker.choose_move()
		a = attacker.attack(attacked, move)
		if a['killed']:
			break
		attacker, attacked = attacked, attacker
