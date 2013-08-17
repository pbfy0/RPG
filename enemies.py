import moves, core
import pprint
p = pprint.PrettyPrinter().pprint

class Enemy(core.Entity):
	stats = {}
	moves = []
	xp = 0
	def __init__(self):
		self.stats = dict(self.stats)
		self.moves = self.moves[:]
		self.set_stats()

class Slime(Enemy):
	level = 1
	stats = dict(hp=20, mp=12, attack=14, defense=10, wisdom=12, speed=10)
	moves = [moves.shock, moves.punch]
	xp = 4

@core.name('War dog')
class WarDog(Enemy):
	level = 1
	stats = dict(hp=15, mp=0, attack=22, defense=14, wisdom=0, speed=18)
	moves = [moves.bite]
	xp = 5
class Zombie(Enemy):
	level = 1
	stats = dict(hp=25, mp=12, attack=18, defense=16, wisdom=12, speed=16)
	moves = [moves.punch, moves.kick, moves.chill]
	xp = 6
class Wizrobe(Enemy):
	level = 1
	stats = dict(hp=15, mp=30, attack=12, defense=14, wisdom=28, speed=15)
	moves = [moves.flame, moves.heal]
	xp = 6
@core.name('King Zombie')
class KingZombie(Enemy):
	level = 15
	stats = dict(hp=200, mp=50, attack=30, defense=25, wisdom=20, speed=30)
	moves = [moves.kick, moves.chill, moves.heal]
	xp = 30

enemies = [Slime, WarDog, Zombie, Wizrobe, KingZombie]