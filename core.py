import races, classes, moves
import random


class Entity(object):
	def set_stats(self):
		#self.stats = dict(hp=0, mp=0, attack=0, defense=0, wisdom=0, speed=0)
		self.hp = self.stats['hp']
		self.mp = self.stats['mp']
	def attack(self, other, move):
		print('{name} used {move}'.format(name=str(self), move=move))
		m = move.use(self, other)
		if move.__class__ == moves.HealingMove:
			self.heal(m['heal'])
			m['killed'] = False
		else:
			if m['type'] == moves.miss: print('Miss!')
			if m['type'] == moves.crit: print('Crit!')
			m['killed'] = self.deal_damage(other, m['damage'])
		return m
	def deal_damage(self, other, n):
		other.take_damage(n)
		if other.hp <= 0:
			other.die()
			self.killed(other)
			return True
		return False
	def take_damage(self, n):
		self.hp -= n
		print('{name} took {damage} damage!'.format(name=str(self), damage=n))
	def heal(self, n):
		self.hp += n
		print('{name} healed {n} HP!'.format(name=str(self), n=n))
	def every_round(self):
		self.hp = min(self.hp + 1, self.stats['hp'])
		self.mp = min(self.mp + self.stats['wisdom']/10, self.stats['mp'])
	def choose_move(self):
		return random.choice(self.moves)
	def __str__(self):
		return self.__class__.__name__
	def die(self):
		print('{name} died'.format(name=str(self)))
	def killed(self, other):
		pass

class Player(races.BaseRace, classes.BaseClass, Entity):
	def __init__(self, race, class_, name):
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
			self.stats[i] = self.bases[i] + (self.bases[i]/4) * self.multipliers[i] * self.level
		if lv_up:
			self.set_stats()
	def every_round(self):
		Entity.every_round(self)
		print('HP: {cur} / {max}'.format(cur=self.hp, max=self.stats['hp']))
	def choose_move(self):
		move = None
		while not move in self.moves:
			movestring = ''
			while not movestring in moves.moves:
				movestring = input('What move do you want to use? ')
			move = moves.moves[movestring]
		return move
	def die(self):
		Entity.die(self)
		self.level -= 1
		self.xp = 0
		self.update_stats()
		self.set_stats()
		print('You died. Respawning. One level lost.')
	def killed(self, other):
		self.xp += other.xp
		self.update_stats()
	def __str__(self):
		return self.name
