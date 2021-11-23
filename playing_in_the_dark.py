# Här inför vi några moduler som vi behöver för koden
import time
import sys
import random as rand
from playsound import playsound
import random
import multiprocessing
# playsound("bell.mp3")

# GLÖMM INTE ÄNDRA PLANERINGEN OM DU ÄNDRAR KODEN!!!

# De tre olika scenarios som kan förekomma när man öppnar dörrarna
scenarios = ["Monster", "Trap", "Treasure"]

# p.terminate()

# Klassen "player" som huvudkaraktären kommer att få


class Player:
    def __init__(self, HP, STR, LVL, BAG):
        self.HP = HP
        self.STR = STR
        self.LVL = LVL
        self.BAG = BAG


class Item:
    def __init__(self, STR):
        self.STR = STR
        print()


# Bokstav för bokstav print, för en mer långsam och förstårbar upplevelse

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0)
        # times.sleep(0.05)

# Bokstav för bokstav print men något snabbare än den ovan


def print_medium(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)

# Funktionen som kommer spelas när du väljer att titta igenom ditt inventory(bag)


def bagcheck(player):
    print_slow("Your inventory:")
    print_slow(player.BAG)
    print("\n")

# Funktionen som kommer spelas när du väljer att titta dina värden (stats)


def statcheck(player):
    print_slow("Your stats in order of HP,STR,LVL")
    print("\n")
    print_slow(str(player.HP))
    print("\n")
    print_slow(str(player.STR))
    print("\n")
    print_slow(str(player.LVL))
    print("\n")


def monsterfight(player):
    monsterstr = random.randint(2, 8)
    print_medium("You have encountered a monster!")
    print("\n")
    time.sleep(2)
    if monsterstr < player.STR:
        print_medium("You won the battle and gained 1 LVL!")
        player.LVL = player.LVL + 1
        print("\n")
    else:
        print_medium("You lost the battle and lost 1 HP")
        print("\n")
    time.sleep(2)


def open_chest(player):
    Blade = Item(2)
    Dagger = Item(1)
    Shortsword = Item(3)
    Excalibur = Item(5)
    item_list = [Blade, Dagger, Shortsword, Excalibur]
    prize = random.choice(item_list)
    if len(player.BAG) < 5:
        player.BAG.append(prize)
    else:
        print_slow(
            "Your inventory is full! Would you like to swap an item?: (Yes/No)")
        choice = input().lower().strip()
        if choice == "yes":
            print(player.BAG)
            print_slow("Select an item index (0-4) that you would like to swap")
            index = int(input().strip())
            player.BAG.pop(index)
            player.BAG.append(prize)
        if choice == "no":
            print_slow("Alright then...")


def trap(player):
    damage = random.randint(1, 3)
    print_medium("You fell into a trap, and took damage: ")
    print_slow(str(damage))
    player.HP = player.HP - damage


# Skapar lite klar yta i termninalen (/n skippar en rad)

def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# ifall ett alternativ som inte finns skrivs in (eller en felstavning), så skicker denna tillbaks dig till frågan


def again1():
    time.sleep(1)
    print_slow("Please enter a valid answer")
    clear()
    start()

# Functionen som startar igång spelet


def start():
    #p = multiprocessing.Process(target=playsound, args=("intro.mp3",))
    # p.start()
    player = Player(10, 3, 1, [])
    print_slow("Would you like to start the game? (Yes/No): ")
    play = input().lower().strip()
    if play == "yes":

        print_slow("Would you like a tutorial? (Yes/No): ")
        want_tutorial = input().lower().strip()
        if want_tutorial == "yes":
            tutorial()
        elif want_tutorial == "no":
            intro()
            playloop(player)
        elif play != "yes" or "no":
            again1()
    elif play == "no":
        print_slow("Maybe next time")
    elif play != "yes" or "no":
        again1()

# Förklaring till hur spelet fungerar och spelas


def tutorial():
    print_medium("Welcome to our game! It is quite simple. You will follow a charachter that will explore multiple rooms, collecting items and treasure, fighting monsters and (hopefully not) dealing with traps")
    print("\n")
    time.sleep(1)
    print_medium("In each room you will be able to chose which action you want to execute. To open one of the doors: type open. To check stats: type stats. And if you want to check your bag: type bag")
    print("\n")
    time.sleep(1)
    print_medium(
        "The goal of the game is to get your LVL from 1 to 10, without dropping you HP below")
    print("\n")
    time.sleep(1)
    print_medium("A trap room will deal a random amount of damage to your HP capped at 3. The treasure rooms will have a item that you can bring along to boost your strength. You can carry 5 items at a time. Lastly the monster room, where you will fight a monster with a random strength. If you have more strength than the monster, you win and gain 1 LVL while if you have less strength than the monster, you lose and forfeit 1 HP  ")
    print("\n")
    time.sleep(1)
    print_medium("Pretty simple huh? Lets get this going shall we?")
    print("\n")
    time.sleep(2)
    print("\n\n")


# Introducerar spelets plats för att skapa atmosfär (mellan varje rad text printas en blank rad, och sedan är det en 1 sekunds paus innan nästa rad)

def intro():
    print("\n")
    print_slow("Darkness")
    time.sleep(1)
    print("\n")
    print_slow("Nothing but darkness")
    time.sleep(1)
    print("\n")
    print_slow(
        "You feel around you with your hands, struggling to understand what is going on")
    time.sleep(1)
    print("\n")
    print_slow("The ground is cold to the touch")
    time.sleep(1)
    print("\n")
    print_slow("You stand up and reach for your phone")
    time.sleep(1)
    print("\n")
    print_slow("No cell connection...")
    time.sleep(1)
    print("\n")
    print_slow("You turn on the flashlight and look around")
    time.sleep(1)
    print("\n")
    print_slow("I gotta get out of here")
    time.sleep(1)
    print("\n")
    time.sleep(2)
    print_slow("Walking a couple of meters reveales 3 identical doors.")
    print("\n")
    time.sleep(1)


# Spelets loop som kör igenom spelet.

def playloop(player: Player):
    while player.HP > 0 or player.LVL < 10:
        print_slow("What would you like to do?")
        print("\n")
        print_slow(
            "Would you like to: open a door, check stats or check inventory? ")
        choice = input().lower().strip()
        if choice == "bag":
            bagcheck(player)
        if choice == "stats":
            statcheck(player)
        if choice == "open":
            print_slow(
                "Which door looks the most interesting..? Door 1, 2 or 3? ")
            door_choice = input().lower().strip()
            if door_choice in ["1", "2", "3"]:
                scen = random.choice(scenarios)
            if scen == "Monster":
                monsterfight(player)
            if scen == "Treasure":
                open_chest(player)
            if scen == "Trap":
                trap(player)


clear()
start()
