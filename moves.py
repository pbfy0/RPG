import random, math
heal_t = -1
miss = 0
hit = 1
crit = 2
class Move(object):
	def __init__(self, name, basepower, stat):
		self.name = name
		self.basepower = basepower
		self.type = 'damage'
		self.stat = stat
	def power(self, user):
		return user.stats[self.stat]/2+self.basepower/5
	def __str__(self):
		return self.name

class PhysicalMove(Move):
	def __init__(self, name, basepower):
		super().__init__(name, basepower, 'attack')
	def use(self, user, on):
		damage = self.power(user) - on.stats['defense']/4
		ret = random.choice((miss, hit, hit, hit, hit, hit, hit, hit, hit, crit))
		if ret != hit: print('Miss!' if ret == miss else 'Crit!')
		damage *= ret
		user.deal_damage(on, damage)
	def desc(self):
		return '{name}: {basepower} damage'.format_map(self.__dict__)

class MagicMove(Move):
	def __init__(self, name, basepower, cost):
		super().__init__(name, basepower, 'wisdom')
		self.cost = cost
	def use(self, caster, at=None):
		if caster.mp >= self.cost:
			caster.mp -= self.cost;
			self.cast(caster, at)
		else:
			print('Out of MP')
	def cast(self, caster, at):
		damage = self.power(caster)
		caster.deal_damage(at, damage)
	def desc(self):
		return '{name}: {basepower} damage, {cost} cost'.format_map(self.__dict__)
class HealingMove(MagicMove):
	def __init__(self, name, basepower, cost):
		super().__init__(name, basepower, cost)
		self.type = 'heal'
	def cast(self, caster, at):
		caster.heal(self.power(caster))
	def desc(self):
		return '{name}: {basepower} healing, {cost} cost'.format_map(self.__dict__)
punch = PhysicalMove('Punch', 30)
kick = PhysicalMove('Kick', 50)
bite = PhysicalMove('Bite', 40)
stab = PhysicalMove('Stab', 80)
firepunch = PhysicalMove('Fire Punch', 70)
thunderpunch = PhysicalMove('Thunder Punch', 70)
icepunch = PhysicalMove('Ice Punch', 70)
lunarbash = PhysicalMove('Lunar Bash', 80)
solarsmash = PhysicalMove('Solar Smash', 80)
shieldbash = PhysicalMove('Shield Bash', 35) # To add: stun

flame = MagicMove('Flame', 50, 2)
chill = MagicMove('Chill', 50, 2)
shock = MagicMove('Shock', 50, 2)
darkstar = MagicMove('Dark Star', 60, 5)
lightray = MagicMove('Light Ray', 60, 5)

heal = HealingMove('Heal', 20, 2)
bless = HealingMove('Bless', 50, 6)

moves = dict(punch=punch, kick=kick, bite=bite, stab=stab, firepunch=firepunch, thunderpunch=thunderpunch, icepunch=icepunch, lunarbash=lunarbash, solarsmash=solarsmash, flame=flame, chill=chill, shock=shock, darkstar=darkstar, lightray=lightray, heal=heal, bless=bless)