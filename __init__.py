import pprint
import core, races, classes, enemies, moves
import random
p = pprint.PrettyPrinter().pprint

unlocked = dict(gladiator=False, sage=False, saint=False, joker=False, master=False)

name = input('Name: ').capitalize()
race = core.prompt('Race: ', races.races)
class_ = core.prompt('Class: ', classes.classes)
player = type('Player', (core.Player, race, class_), {})(race, class_, name)
for i in player.moves: print(i.desc())
#p(x.__dict__)
while True:
	enemy_choices, dl = [], 2
	while len(enemy_choices) == 0:
		enemy_choices = [x for x in enemies.enemies if abs(player.level - x.level) < dl]
		dl += 1
	enemy = random.choice(enemy_choices)()
	print('A {} has spotted you!'.format(str(enemy).lower()))
	ps, es = (x*random.random()/4+0.875 for x in (player.stats['speed'], enemy.stats['speed']))
	attacker, attacked = (player, enemy) if ps > es else (enemy, player)
	while True:
		attacker.every_round()
		move = attacker.choose_move()
		a = attacker.attack(attacked, move)
		if attacked.dead:
			print()
			break
		attacker, attacked = attacked, attacker
