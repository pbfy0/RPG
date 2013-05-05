import pprint
import core, races, classes, enemies, moves
import random
p = pprint.PrettyPrinter().pprint

unlocked = dict(gladiator=False, sage=False, saint=False, joker=False, master=False)
def choose_race():
	race = ''
	while not race in races.races:
		race = input('Race: ').lower()
	return races.races[race]
def choose_class():
	cls = ''
	while not cls in classes.classes:
		cls = input('Class: ').lower()
	return classes.classes[cls]

name = input('Name: ')
race = choose_race()
cls = choose_class()
player = core.Player(race, cls, name)
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
	attacker, attacked = (player, ce) if player.stats['speed'] > ce.stats['speed'] else (ce, player)
	while True:
		attacker.every_round()
		move = attacker.choose_move()
		a = attacker.attack(attacked, move)
		if a['killed']:
			break
		attacker, attacked = attacked, attacker
