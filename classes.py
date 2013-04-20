import moves

class BaseClass(object):
	def __init__(self):
		self.moves = [moves.punch]
		#self.bases = {} #dict(hp=0, mp=0, attack=0, defense=0, wisdom=0, speed=0)

class Warrior(BaseClass):
	def __init__(self):
		BaseClass.__init__(self)
		self.bases = dict(hp=19, mp=4, attack=23, defense=16, wisdom=7, speed=15)
		self.moves += [moves.kick]
class Mage(BaseClass):
	def __init__(self):
		BaseClass.__init__(self)
		self.bases = dict(hp=12, mp=20, attack=6, defense=9, wisdom=22, speed=13)
		self.moves += [moves.flame]
class Priest(BaseClass):
	def __init__(self):
		BaseClass.__init__(self)
		self.bases = {'speed': 14, 'wisdom': 23, 'hp': 11, 'attack': 8, 'mp': 19, 'defense': 5}
		self.moves += [moves.heal]
class Bard(BaseClass):
	def __init__(self):
		BaseClass.__init__(self)
		self.bases = {'hp': 18, 'speed': 11, 'wisdom': 13, 'attack': 14, 'defense': 13, 'mp': 11}
		self.moves += [moves.chill]
class Ninja(BaseClass):
	def __init__(self):
		BaseClass.__init__(self)
		self.bases = {'attack': 18, 'defense': 14, 'mp': 5, 'hp': 12, 'wisdom': 7, 'speed': 24}
		self.moves += [moves.agility]
class Guard(BaseClass):
	def __init__(self):
		BaseClass.__init__(self)
		self.bases = {'mp': 6, 'attack': 15, 'speed': 10, 'hp': 22, 'defense': 23, 'wisdom': 4}
		self.moves += [moves.defend]
# advanced classes
class Gladiator(BaseClass):
	def __init__(self):
		BaseClass.__init__(self)
		self.bases = {'mp': 8, 'attack': 30, 'defense': 18, 'speed': 14, 'wisdom': 8, 'hp': 22}
class Sage(BaseClass):
	def __init__(self):
		BaseClass.__init__(self)
		self.bases = {'wisdom': 28, 'defense': 8, 'hp': 12, 'speed': 16, 'attack': 4, 'mp': 32}
class Saint(BaseClass):
	def __init__(self):
		BaseClass.__init__(self)
		self.bases = {'defense': 7, 'attack': 7, 'mp': 24, 'hp': 12, 'wisdom': 32, 'speed': 18}
class Joker(BaseClass):
	def __init__(self):
		BaseClass.__init__(self)
		self.bases = {'wisdom': 16, 'hp': 20, 'mp': 16, 'speed': 16, 'attack': 16, 'defense': 16}
class Master(BaseClass):
	def __init__(self):
		BaseClass.__init__(self)
		self.bases = {'mp': 10, 'attack': 23, 'speed': 30, 'defense': 12, 'hp': 15, 'wisdom': 10}
class Paladin(BaseClass):
	def __init__(self):
		BaseClass.__init__(self)
		self.bases = {'attack': 21, 'defense': 24, 'wisdom': 12, 'speed': 2, 'mp': 14, 'hp': 27}

classes = dict(warrior=Warrior, mage=Mage, priest=Priest, bard=Bard, ninja=Ninja, guard=Guard, gladiator=Gladiator, sage=Sage, saint=Saint, joker=Joker, master=Master, paladin=Paladin)