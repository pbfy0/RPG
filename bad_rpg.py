# A simple text based RPG game
# Bobby Clarke

# I made this a long time ago
# It uses many bad and sub-optimal practices
# as such, I will not work on it any further 

# GNU General Public License 3.0

#indev 0.007

# To Do: 

# add more moves
# add more mooks
# add enemy AI
# make moves cost MP
# add currency
# add death penalty
# add racial skills ?
# add analyse option
# add battle menu(attack, run)
# Help and printing move list and stats
# make usemove not use eval() ( for move in player.moves )
# add buff moves
# add class unlocking
# add saving / loading
# add move learning on level up


import random
import pickle
#import math
#import pygame

gladiator_unlocked = False,
sage_unlocked = False,
saint_unlocked = False,
joker_unlocked = False,
master_unlocked = False,
paladin_unlocked = False

unlocks = (gladiator_unlocked,
           sage_unlocked,
           saint_unlocked,
           joker_unlocked,
           master_unlocked,
           paladin_unlocked)

unlocks_file = open("unlocks.dat", "wb")

pickle.dump(unlocks, unlocks_file)

unlocks_file.close()



class player:
    # The Player
    
    def playerclass(self, warrior = False, mage = False, priest = False,
                    bard = False, ninja = False, guard = False,
                    gladiator = False, sage = False, saint = False,
                    joker = False, master = False, paladin = False):
        # The player's class and base stats

        # Basic classes
        if warrior:
            playerclass = "warrior"
            baseHP = 19
            baseMP = 4
            baseATK = 23
            baseDEF = 16
            baseWIS = 7
            baseSPD = 11 #80
        elif mage:
            playerclass = "mage"
            baseHP = 12
            baseMP = 20
            baseATK = 6
            baseDEF = 9
            baseWIS = 22
            baseSPD = 13 #80
        elif priest:
            playerclass = "priest"
            baseHP = 11
            baseMP = 19
            baseATK = 8
            baseDEF = 5
            baseWIS = 23
            baseSPD = 14 #80
        elif bard:
            playerclass = "bard"
            baseHP = 18
            baseMP = 11
            baseATK = 14
            baseDEF = 13
            baseWIS = 13
            baseSPD = 11 #80
        elif ninja:
            playerclass = "ninja"
            baseHP = 12
            baseMP = 5
            baseATK = 18
            baseDEF = 14
            baseWIS = 7
            baseSPD = 24 #80
        elif guard:
            playerclass = "guard"
            baseHP = 22
            baseMP = 6
            baseATK = 15
            baseDEF = 23
            baseWIS = 4
            baseSPD = 10 #80
        #   #   #   #   #

        # Advanced Classes
        elif gladiator:
            playerclass = "gladiator"
            baseHP = 22
            baseMP = 8
            baseATK = 30
            baseDEF = 18 
            baseWIS = 8
            baseSPD = 14 #100
        elif sage:
            playerclass = "sage"
            baseHP = 12
            baseMP = 32
            baseATK = 4
            baseDEF = 8
            baseWIS = 28
            baseSPD = 16 #100
        elif saint:
            playerclass = "saint"
            baseHP = 12
            baseMP = 24
            baseATK = 7
            baseDEF = 7 
            baseWIS = 32
            baseSPD = 18 #100
        elif joker:
            playerclass = "joker"
            baseHP = 20
            baseMP = 16
            baseATK = 16
            baseDEF = 16
            baseWIS = 16
            baseSPD = 16 #100
        elif master:
            playerclass = "master"
            baseHP = 15
            baseMP = 10
            baseATK = 23
            baseDEF = 12
            baseWIS = 10
            baseSPD = 30 #100
        elif paladin:
            playerclass = "paladin"
            baseHP = 27
            baseMP = 14
            baseATK = 21
            baseDEF = 24
            baseWIS = 12
            baseSPD = 2 #100
        #   #   #   #   #

        def unlock(readorwrite):
            if readorwrite == "read":
                open("unlocks.dat", "rb")
            elif readorwrite == "write":
                open ("unlocks.dat", "rb")
            

        return playerclass, baseHP, baseMP, baseATK, baseDEF, baseWIS, baseSPD

    def race(race):
        #The player's race to be used for stat bonuses
        return race

    def level(self, plrlevel, exp):
        # determining the player's level, experience,
        # and experience required to level up
        oldlevel = plrlevel

        #This is the level up experiece formula, subject to change
        exp2level = int(round((plrlevel ** 3 / 12) + plrlevel * 4))
        
        while exp >= exp2level:
            expcarry = exp - exp2level
            exp = expcarry

            plrlevel += 1
            exp2level = plrlevel

            exp2level = int(round((plrlevel ** 3 / 12) + plrlevel * 4))

        return plrlevel, exp2level, exp, oldlevel

    def stats(self, plrlevel, race, baseHP, baseMP, baseATK, baseDEF, baseWIS, baseSPD):
        #Determining the player's stats from class, race and level
        if race == "human":
            HP = int(round(baseHP + (int(round(baseHP / 4 // 1)) * plrlevel) * 1.1))
            MP = int(round(baseMP + (baseMP / 4 // 1 * plrlevel) * 1.1 ))
            attack = int(round(baseATK + (baseATK / 4 * plrlevel) * 1.1))
            defense = int(round(baseDEF + (baseDEF / 4  * plrlevel) * 1.1))
            wisdom = int(round(baseWIS + (baseWIS / 4 * plrlevel) * 1.1))
            speed = int(round(baseSPD + (baseSPD / 4 * plrlevel) * 1.1 // 1))

        elif race == "elf":
            HP = int(round(baseHP + (baseHP / 4 * plrlevel)))
            MP = int(round(baseMP + (baseMP / 4 * plrlevel) * 1.25))
            attack = int(round(baseATK + (baseATK / 4 * plrlevel)))
            defense = int(round(baseDEF + (baseDEF / 4 * plrlevel)))
            wisdom = int(round(baseWIS + (baseWIS / 4 * plrlevel) * 1.25))
            speed = int(round(baseSPD + (baseSPD / 4 * plrlevel) * 1.25))

        elif race == "orc":
            HP = int(round(baseHP + (baseHP / 4 * plrlevel) * 1.25))
            MP = int(round(baseMP + (baseMP / 4 * plrlevel)))
            attack = int(round(baseATK + (baseATK / 4 * plrlevel) * 1.25))
            defense = int(round(baseDEF + (baseDEF / 4 * plrlevel) * 1.25))
            wisdom = int(round(baseWIS + (baseWIS / 4 * plrlevel)))
            speed = int(round(baseSPD + (baseSPD / 4 * plrlevel)))
            

        return HP, MP, attack, defense, wisdom, speed

    def moves(playerclass, plrlevel):
        #The player's moves
        if playerclass == "warrior":
            moves = [punch, kick]
        elif playerclass == "mage":
            moves = [punch, flame]
        elif playerclass == "priest":
            moves = [punch, heal]
        elif playerclass == "bard":
            moves = [punch, chill]
        elif playerclass == "ninja":
            moves = [punch, agility]
        elif playerclass == "guard":
            moves = [punch, defend]

        return moves

    def name(name):
        #The player's name
        return name
    
    def showmoves(self):
        for move in self.moves:
            print(move[0] + ":", move[1], "power", move[2], move[3])
        

class enemy:
    #Enemies to be fought in battle
    #Incomplete
    def moves(moves = []):
        #The enemy's moves
        return moves
        
    def stats(HP, MP, strength, defense, wisdom, speed):
        #the enemy's stats
        return HP, MP, strength, defense, wisdom, speed
    def name(name):
        #the enemy's name
        return name
    
class move:
    #moves to be used by players and enemies
    def physical(name, power, element, usestat = "attack"):
        #Physical attacks using the attack stat
        return name, power, element, usestat
    def special(name, power, element, usestat = "wisdom"):
        #Special / magical attacks using the wisdom stat
        return name, power, element, usestat
    def buff(name, power, stat):
        #Buff moves to increase stats
        stat *= power
        return stat
    def heal(name, power, usestat = "heal"):
        return name, power, usestat
    
    

### All moves in the game ###
# Physical
punch = move.physical("Punch", 30, "normal")
kick = move.physical("Kick", 50, "normal")
bite = move.physical("Bite", 40, "dark")
stab = move.physical("Stab", 80, "normal")
firepunch = move.physical("Fire Punch", 70, "fire")
thunderpunch = move.physical("Thunder Punch", 70, "electric")
icepunch = move.physical("Ice Punch", 70, "ice")
lunarbash = move.physical("Lunar Bash", 80, "dark")
solarsmash = move.physical("Solar Smash", 80, "light")

#Special
flame = move.special("Flame", 50, "fire")
chill = move.special("Chill", 50, "ice")
shock = move.special("Shock", 50, "electric")
darkstar = move.special("Dark Star", 60, "dark")
lightray = move.special("Light Ray", 60, "light")

#Healing

heal = move.heal("Heal", 20)
bless = move.heal("Bless", 50)


# Buffs
workup = "workup"
defend = "defend"
agility = "agility"

#####################

### All enemies in the game ###

# Level 1
slime = enemy()
slime.name = enemy.name("Slime")
slime.stats = enemy.stats(20, 12, 14, 10, 12, 10)
slime.moves = enemy.moves([shock, punch])
slime.exp = 4

wardog = enemy()
wardog.name = enemy.name("War Dog")
wardog.stats = enemy.stats(15, 0, 22, 14, 0, 18)
wardog.moves = enemy.moves([bite])
wardog.exp = 5

zombie = enemy()
zombie.name = enemy.name("Zombie")
zombie.stats = enemy.stats(25, 12, 18, 16, 12, 16)
zombie.moves = ([punch, kick, chill])
zombie.exp = 6

wizrobe = enemy()
wizrobe.name = "Wizrobe"
wizrobe.stats = (15, 30, 12, 14, 28, 15)
wizrobe.moves = [flame, heal]
wizrobe.exp = 6

level_1_enemies = (slime, wardog, zombie, wizrobe)

# Bosses
kingzombie = enemy()
kingzombie.name = enemy.name("King Zombie")
kingzombie.stats = enemy.stats(200, 50, 30, 25, 20, 30)
kingzombie.moves = enemy.moves([kick, chill, heal]) 
kingzombie.exp = 30


def char_build():
    #Creating a character / player
    PLR = player()

    plrname = input("Name your character: ")
    PLR.name = player.name(plrname)

    race_chosen = False
    races = ("human", "orc", "elf")
    
    while not race_chosen:
        print("\nRaces: Human, Orc, Elf")
        race = input("Choose your race: ").lower()

        if race in races:
            PLR.race = player.race(race)
            race_chosen = True

        else:
            print("That race is not available")
    
    print("\nClasses: Warrior, Mage, Priest, Bard, Ninja, Guard")

    class_chosen = False
    while not class_chosen:
        classchoice = input("Choose your class: ")
        classchoice = classchoice.lower()
    
        if classchoice == "warrior":
            PLR.playerclass, PLR.baseHP, PLR.baseMP, PLR.baseATK, PLR.baseDEF, PLR.baseWIS, PLR.baseSPD = PLR.playerclass(warrior = True)
            class_chosen = True
        elif classchoice == "mage":
            PLR.playerclass, PLR.baseHP, PLR.baseMP, PLR.baseATK, PLR.baseDEF, PLR.baseWIS, PLR.baseSPD = PLR.playerclass(mage = True)
            class_chosen = True
        elif classchoice == "priest":
            PLR.playerclass, PLR.baseHP, PLR.baseMP, PLR.baseATK, PLR.baseDEF, PLR.baseWIS, PLR.baseSPD = PLR.playerclass(priest = True)
            class_chosen = True
        elif classchoice == "bard":
            PLR.playerclass, PLR.baseHP, PLR.baseMP, PLR.baseATK, PLR.baseDEF, PLR.baseWIS, PLR.baseSPD = PLR.playerclass(bard = True)
            class_chosen = True
        elif classchoice == "ninja":
            PLR.playerclass, PLR.baseHP, PLR.baseMP, PLR.baseATK, PLR.baseDEF, PLR.baseWIS, PLR.baseSPD = PLR.playerclass(ninja = True)
            class_chosen = True
        elif classchoice == "guard":
            PLR.playerclass, PLR.baseHP, PLR.baseMP, PLR.baseATK, PLR.baseDEF, PLR.baseWIS, PLR.baseSPD = PLR.playerclass(guard = True)
            class_chosen = True
        else:
            print("That class is not available")

    PLR.plrlevel, PLR.exp2level, PLR.exp, PLR.oldlevel = PLR.level(plrlevel = 1, exp = 0)

    PLR.HP, PLR.MP, PLR.attack, PLR.defense, PLR.wisdom, PLR.speed = PLR.stats(PLR.plrlevel, PLR.race, PLR.baseHP, PLR.baseMP, PLR.baseATK, PLR.baseDEF, PLR.baseWIS, PLR.baseSPD)

    PLR.moves = player.moves(PLR.playerclass, PLR.plrlevel)

    PLR.stats = PLR.HP, PLR.MP, PLR.attack, PLR.defense, PLR.wisdom, PLR.speed

    print("\nYour moves are:")
    PLR.showmoves()

    return PLR

def battle(plr, enemy):
    # The battle scene, player vs enemy
    print("\n" + enemy.name, "wants to fight")

    enemy.HP = enemy.stats[0]
    enemy.MP = enemy.stats[1]
    enemy.attack = enemy.stats[2]
    enemy.defense = enemy.stats[3]
    enemy.wisdom = enemy.stats[4]
    enemy.speed = enemy.stats[5]

    plr.hpleft = plr.HP
    enemy.hpleft = enemy.HP
    
    turns = ("player", "enemy")
    if plr.speed > enemy.speed:
        turn = "player"
    elif enemy.speed > plr.speed:
        turn = "enemy"
    else:
        turn = random.choice(turns)
        
    resolved = False
    while not resolved:
        usemove = ""
        if turn == "player":
            print("HP", plr.hpleft, "/", plr.HP)
            while not usemove:
                usemove = input("\nWhat move will you use? ")
                if usemove == 'help':
                                 print("\nYour moves are:")
                                 PLR.showmoves()
                                 print(f'enemy hp:{enemy.HP}')
                                 print(f'enemy mp:{enemy.MP}')
                try:
                    usemove = eval(usemove) # What move will you use? exec("import code; code.interact(local=locals())")
                except:
                    print("Invalid Move")
                    usemove = ""
        
            if usemove in plr.moves:

                if usemove [2] == "heal":
                    healby = int(round((usemove[1] + plr.wisdom) / 4))
                    plr.hpleft += healby
                    
                    if plr.hpleft > plr.HP:
                        plr.hpleft = plr.HP
                    print("HP restored by", healby, "points")
                    
                    turn = "enemy"
                
                elif usemove[3] == "attack":
                    # Damage formula subject to change
                    damage = int(round((plr.attack / 2) + (usemove[1] / 5)))
                    damage -= int(round(enemy.defense / 4))
                    #Critical hits and missing
                    critmiss = random.randint(1, 10)
                    crit = False
                    miss = False
                    if critmiss == 9:
                        #Miss
                        damage = 0
                        miss = True
                    elif critmiss == 10:
                        #Critical hit
                        damage *= 2
                        crit = True

                        
                    if damage > 0:
                        damage += random.randint(int(round(-damage * 0.1)), int(round(damage * 0.1)))
                
                    enemy.hpleft -= damage
                    if not miss:
                        if crit:
                            print("Critical Hit!")
                        
                        print(damage, "damage!")

                    else:
                        print("You missed!")

                    turn = "enemy"

                elif usemove[3] == "wisdom":
                    damage = int(round((plr.wisdom / 2) + (usemove[1] / 5)))
                    damage -= int(round(enemy.defense / 4))

                    #Critical hits and missing
                    critmiss = random.randint(1, 10)
                    crit = False
                    miss = False
                    if critmiss == 9:
                        #Miss
                        damage = 0
                        miss = True
                    elif critmiss == 10:
                        #Critical hit
                        damage *= 2
                        crit = True
                        
                    if damage > 0:
                        damage += random.randint(int(round(-damage * 0.1)), int(round(damage * 0.1)))

                    
                    enemy.hpleft -= damage
                    
                    if not miss:
                        if crit:
                            print("Critical Hit!")
                        print(damage, "damage!")

                    else:
                        print("You missed!")

                    turn = "enemy"


            else:
                print("You do not know that move")

                

        elif turn == "enemy":
            usemove = random.choice(enemy.moves)

            if usemove [2] == "heal":
                    healby = int(round((usemove[1] + enemy.wisdom) / 4))
                    enemy.hpleft += healby
                    if enemy.hpleft > enemy.HP:
                        enemy.hpleft = enemy.HP
                    print("\n", enemy.name, "used", usemove[0])
                    
                    turn = "player"
            
            elif usemove[3] == "attack":
                damage = int(round((enemy.attack / 2) + (usemove[1] / 5)))
                damage -= int(round(plr.defense / 4))

                    #Critical hits and missing
                critmiss = random.randint(1, 10)
                crit = False
                miss = False
                if critmiss == 9:
                    #Miss
                    damage = 0
                    miss = True
                elif critmiss == 10:
                    #Critical hit
                    damage *= 2
                    crit = True

                if not miss:
                    if damage < 1:
                        damage = 1

                damage += random.randint(int(round(-damage * 0.1)), int(round(damage * 0.1 )))

                plr.hpleft -= damage
                
                print("\n", enemy.name, "used" , usemove[0])

                if not miss:
                    if crit:
                        print("Critical Hit!")
                    print("you took", damage, "damage!")

                else:
                    print(enemy.name, "missed!")

                turn = "player"

            elif usemove[3] == "wisdom":
                damage = int(round((enemy.wisdom / 2) + (usemove[1] / 5)))
                damage -= int(round(plr.defense / 4))

                #Critical hits and missing
                critmiss = random.randint(1, 10)
                crit = False
                miss = False
                if critmiss == 9:
                    #Miss
                    damage = 0
                    miss = True
                elif critmiss == 10:
                    #Critical hit
                    damage *= 2
                    crit = True
                    
                if damage > 0:
                    damage += random.randint(int(round(-damage * 0.1)), int(round(damage * 0.1)))

                plr.hpleft -= damage

                print("\n", enemy.name, "used" , usemove[0])
                if not miss:
                    if crit:
                        print("Critical hit!")
                    
                    print("you took", damage, "damage!")
                else:
                    print(enemy.name, "missed!")

                turn = "player"


        if plr.hpleft <= 0 or enemy.hpleft <= 0:
            resolved = True

            if plr.hpleft <= 0:
                print("\nYou lose!")
            elif enemy.hpleft <= 0:
                print("You win!")
                print("You got", enemy.exp, "exp!")
                plr.exp += enemy.exp
                plr.plrlevel, plr.exp2level, plr.exp, plr.oldlevel = player.level(plr, plr.plrlevel, plr.exp)

                if plr.plrlevel > plr.oldlevel:
                    print("You leveled up!, you are now level", plr.plrlevel)
                    plr.HP, plr.MP, plr.attack, plr.defense, plr.wisdom, plr.speed = player.stats(plr, plr.plrlevel, plr.race, plr.baseHP, plr.baseMP, plr.baseATK, plr.baseDEF, plr.baseWIS, plr.baseSPD)

    return plr

def showstats(plr):
    print("\nHP:", plr.HP)
    print("MP:", plr.MP)      
    print("Attack:", plr.attack)
    print("Defense:", plr.defense)
    print("Wisdom:", plr.wisdom)
    print("Speed:", plr.speed)
    
def main():
    plr = char_build()
    
    battle(plr, slime)
    
    for i in range(4):
        battle(plr, random.choice(level_1_enemies))
        
    while True:
        if random.randint(1, 10) == 1:
            battle(plr, kingzombie)
        else:
            battle(plr, random.choice(level_1_enemies))

if __name__ == "__main__":
    main()
