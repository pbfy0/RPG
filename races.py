class BaseRace(object):
	multipliers = dict(hp=1, mp=1, attack=1, defense=1, wisdom=1, speed=1)

def partial(cls):
	mult = dict(cls.__bases__[0].multipliers)
	mult.update(cls.multipliers)
	cls.multipliers = mult
	return cls

class Human(BaseRace):
	name = 'Human'
	multipliers = dict(hp=1.1, mp=1.1, attack=1.1, defense=1.1, wisdom=1.1, speed=1.1)
@partial
class Elf(BaseRace):
	name = 'Elven'
	multipliers = dict(mp=1.25, wisdom=1.25, speed=1.25)
@partial
class Orc(BaseRace):
	name = 'Orcish'
	multipliers = dict(hp=1.25, attack=1.25, defense=1.25)

races = dict(human=Human, elf=Elf, orc=Orc)