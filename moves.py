import random, math
heal_t = -1
miss = 0
hit = 1
crit = 2
intfloor = lambda x: int(math.floor(x))
class Move(object):
	def __init__(self, name, power, stat):
		self.name = name
		self.power = power
		self.type = 'damage'
		self.stat = stat
	def __str__(self):
		return self.name

class PhysicalMove(Move):
	def __init__(self, name, power):
		Move.__init__(self, name, power, 'attack')
	def use(self, user, on):
		damage = (user.stats[self.stat]/2+self.power/5) - on.stats['defense']/4
		n = random.randrange(10)
		ret = hit
		if n == 0: ret = miss
		if n == 9: ret = crit
		damage *= ret
		return dict(damage=intfloor(damage), type=ret)
	def desc(self):
		return '{name}: {power} damage'.format(**self.__dict__)

class MagicMove(Move):
	def __init__(self, name, power, cost):
		Move.__init__(self, name, power, 'wisdom')
		self.cost = cost
	def use(self, caster, at=None):
		if caster.mp >= self.cost:
			caster.mp -= self.cost;
			return self.cast(caster)
		else:
			return dict(damage=0, type=miss)
	def cast(self, caster):
		damage = caster.stats[self.stat]/2+self.power/5
		return dict(damage=intfloor(damage), type=hit)
	def desc(self):
		return '{name}: {power} damage, {cost} cost'.format_map(self.__dict__)
class HealingMove(MagicMove):
	def __init__(self, name, power, cost):
		MagicMove.__init__(self, name, power, cost)
		self.type = 'heal'
	def cast(self, caster):
		return dict(heal=intfloor(self.power), type=heal_t)
	def desc(self):
		return '{name}: {power} healing, {cost} cost'.format_map(self.__dict__)
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