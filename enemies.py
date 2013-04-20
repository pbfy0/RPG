import moves, core
import pprint
p = pprint.PrettyPrinter().pprint

class Enemy(core.Entity):
	def __init__(self):
		self.stats = {}
		self.moves = []
		self.xp = 0
class Slime(Enemy):
	level = 1
	def __init__(self):
		self.stats = dict(hp=20, mp=12, attack=14, defense=10, wisdom=12, speed=10)
		self.set_stats()
		self.moves = [moves.shock, moves.punch]
		self.xp = 4
class WarDog(Enemy):
	level = 1
	def __init__(self):
		self.stats = dict(hp=15, mp=0, attack=22, defense=14, wisdom=0, speed=18)
		self.set_stats()
		self.moves = [moves.bite]
		self.xp = 5
class Zombie(Enemy):
	level = 1
	def __init__(self):
		self.stats = dict(hp=25, mp=12, attack=18, defense=16, wisdom=12, speed=16)
		self.set_stats()
		self.moves = [moves.punch, moves.kick, moves.chill]
		self.xp = 6
class Wizrobe(Enemy):
	level = 1
	def __init__(self):
		self.stats = dict(hp=15, mp=30, attack=12, defense=14, wisdom=28, speed=15)
		self.set_stats()
		self.moves = [moves.flame, moves.heal]
		self.xp = 6
class KingZombie(Enemy):
	level = 5
	def __init__(self):
		self.stats = dict(hp=200, mp=50, attack=30, defense=25, wisdom=20, speed=30)
		self.set_stats()
		self.moves = [moves.kick, moves.chill, moves.heal]
		self.xp = 30

enemies = [Slime, WarDog, Zombie, Wizrobe, KingZombie]