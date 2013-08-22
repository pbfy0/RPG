import races, classes, moves
import random


class Entity(object):
	def set_stats(self):
		#self.stats = dict(hp=0, mp=0, attack=0, defense=0, wisdom=0, speed=0)
		self.hp = self.stats['hp']
		self.mp = self.stats['mp']
	def attack(self, other, move):
		print('{} used {}'.format(self, move))
		move.use(self, other)
	def deal_damage(self, other, n):
		n = int(n)
		other.take_damage(n)
		if other.dead:
			other.die()
			self.killed(other)
			return True
		return False
	@property
	def dead(self):
		return self.hp <= 0
	def take_damage(self, n):
		if n != 0:
			self.hp -= n
			print('{} took {} damage!'.format(self, n))
	def heal(self, n):
		self.hp = min(self.hp + n, self.stats['hp'])
		print('{} healed {} HP!'.format(self, n))
	def every_round(self):
		self.hp = min(self.hp + 1, self.stats['hp'])
		self.mp = min(self.mp + round(self.stats['wisdom']/10), self.stats['mp'])
	def choose_move(self):
		return random.choice(self.moves)
	def __str__(self):
		return type(self).__name__
	def die(self):
		print('{} died'.format(self))
	def killed(self, other):
		pass

class Player(Entity):
	def __init__(self, race, class_, name):
		super().__init__()
		race.__init__(self)
		class_.__init__(self)
		self.stats = {}
		self.level = 1
		self.xp = 0;
		self.update_stats()
		self.set_stats() # here for a good reason
		self.type = race.name + ' ' + class_.__name__
		self.name = name
	def update_stats(self):
		lv_up = False
		if self.xp >= self.level ** 2:
			lv_up = True
			self.xp -= self.level ** 2
			self.level += 1
			print('New level: {level}'.format(level=self.level))
		for i in self.bases:
			self.stats[i] = round(self.bases[i] + (self.bases[i]/4) * self.multipliers[i] * self.level)
		if lv_up:
			self.set_stats()
	def every_round(self):
		super().every_round()
		print('HP: {} / {} MP: {} / {}'.format(self.hp, self.stats['hp'], self.mp, self.stats['mp']))
	def choose_move(self):
		return prompt('What move do you want to use? ', moves.moves)
	def die(self):
		Entity.die(self)
		self.level -= 1
		self.xp = 0
		print('You died. Respawning. One level lost.')
		self.update_stats()
		self.set_stats()
	def killed(self, other):
		self.xp += other.xp
		self.update_stats()
	def __str__(self):
		return self.name

import functools
def arg_deco(func):
	def _wrap(*args, **kwargs):
		@functools.wraps(func)
		def _wrap2(val):
			return func(val, *args, **kwargs)
		return _wrap2
	return _wrap

@arg_deco
def name(x, n):
	x.__name__ = n
	return x

def prompt(prompt, valid):
	v = input(prompt)
	t = '... '.rjust(len(prompt))
	while not v in valid:
		v = input(t)
	return valid[v]