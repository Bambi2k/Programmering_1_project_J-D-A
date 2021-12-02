# Här inför vi några moduler som vi behöver för koden
import time
import sys
import random as rand
import random
import multiprocessing
import threading
from pygame import mixer
import text_functions


# GLÖMM INTE ÄNDRA PLANERINGEN OM DU ÄNDRAR KODEN!!!

# De tre olika scenarios som kan förekomma när man öppnar dörrarna
SCENARIOS = ["Monster", "Monster", "Monster", "Trap", "Treasure", "Treasure"]


# Klassen "player" som huvudkaraktären kommer att få


class Player:
    def __init__(self, HP, STR, LVL, BAG):
        self.HP = HP
        self.STR = STR
        self.LVL = LVL
        self.BAG = BAG


class Item:
    def __init__(self, NAME, STR):
        self.NAME = NAME
        self.STR = STR


def intro_music():
    mixer.init()
    mixer.music.load("intro.mp3")
    mixer.music.set_volume(0.9)


intro = threading.Thread(target=intro_music, args=())


# Funktionen som kommer spelas när du väljer att titta igenom ditt inventory(bag)


def bagcheck(player):
    print("\n")
    bag_list = []
    text_functions.print_slow("Your inventory: ")
    for item in player.BAG:
        bag_list.append(item.NAME)
    print(bag_list)
    print("\n")


# Funktionen som kommer spelas när du väljer att titta dina värden (stats)


def statcheck(player):
    text_functions.print_slow("Your stats in order of HP,STR,LVL")
    print("\n")
    text_functions.print_slow(str(player.HP))
    print("\n")
    text_functions.print_slow(str(player.STR))
    print("\n")
    text_functions.print_slow(str(player.LVL))
    print("\n")


def monsterfight(player):
    monsterstr = random.randint(2, 12)
    print("\n")
    text_functions.print_slow("You have encountered a monster! ")
    text_functions.print_slow("It has a strenghth of: ")
    text_functions.print_slow(str(monsterstr))
    print("\n")
    time.sleep(2)
    if monsterstr < player.STR:
        text_functions.print_slow("You won the battle and gained 1 LVL!")
        player.LVL = player.LVL + 1
        print("\n")
    elif monsterstr == player.STR:
        text_functions.print_slow(
            "The monster and you where evenly matched, and you managed to flee the monster unscathed.")
    else:
        text_functions.print_slow("You lost the battle and lost 1 HP")
        player.HP = player.HP - 1
        print("\n")
    time.sleep(2)


def open_chest(player):
    item_list = [Item("Blade", 2), Item("Dagger", 1), Item("Shortsword", 1),
                 Item("Excalibur", 5), Item("Knife", 1), Item("Katana", 2), Item("Machete", 2), Item("Broadsword", 3)]
    prize = random.choice(item_list)
    while len(player.BAG) == 5:
        print("\n")
        text_functions.print_slow("The chest contained the item: ")
        print("\n")
        text_functions.print_slow(prize.NAME)
        print("\n")
        text_functions.print_slow(
            "Your inventory is full! Would you like to swap an item?: (Yes/No) ")
        choice = input().lower().strip()
        if choice == "yes":
            bagcheck(player)
            text_functions.print_slow(
                "Select an item index (0-4) that you would like to swap: ")
            index = int(input().strip())
            player.BAG.pop(index)
            player.BAG.append(prize)
            print("\n")
            text_functions.print_slow(
                "Your new item has been added to your inventory")
            break
        elif choice == "no":
            text_functions.print_slow("Alright then...")
            break
        else:
            print("\n")
            time.sleep(1)
            text_functions.print_slow("Try again")

    if len(player.BAG) < 5:
        player.BAG.append(prize)
        text_functions.print_slow("You have recieved an item: ")
        print("\n")
        text_functions.print_slow(prize.NAME)


def trap(player):
    damage = random.randint(1, 2)
    print("\n")
    text_functions.print_slow("You fell into a trap, and took damage: ")
    text_functions.print_slow(str(damage))
    player.HP = player.HP - damage
    print("\n")


# ifall ett alternativ som inte finns skrivs in (eller en felstavning), så skicker denna tillbaks dig till frågan

def again():
    time.sleep(1)
    text_functions.print_slow("Please enter a valid answer")
    time.sleep(3)
    text_functions.clear()
    start()


def total_str(player):
    player.STR = 4
    t_str = 0
    for item in player.BAG:
        t_str = t_str + item.STR
    player.STR = player.STR + t_str


# Functionen som startar igång spelet


def start():
    player = Player(10, 4, 1, [])
    text_functions.print_slow("Would you like to start the game? (Yes/No): ")
    play = input().lower().strip()
    if play == "yes":
        text_functions.print_slow("Would you like a tutorial? (Yes/No): ")
        want_tutorial = input().lower().strip()
        if want_tutorial == "yes":
            text_functions.tutorial()
            text_functions.intro()
            playloop(player)
        elif want_tutorial == "no":
            text_functions.intro()
            playloop(player)
        elif play != "yes" or "no":
            again()
    elif play == "no":
        text_functions.print_slow("Maybe next time")
    elif play != "yes" or "no":
        again()


# Spelets loop som kör igenom spelet.

def playloop(player: Player):
    while player.HP > 0 and player.LVL < 10:
        total_str(player)
        print("\n")
        text_functions.print_slow(
            "Would you like to: open a door(open), check stats(stats) or check inventory(bag)? ")
        choice = input().lower().strip()
        if choice == "bag":
            bagcheck(player)
        if choice == "stats":
            statcheck(player)
        if choice == "open":
            text_functions.print_slow(
                "Which door would you like to choose? Door 1, 2 or 3? ")
            door_choice = input().lower().strip()
            if door_choice in ["1", "2", "3"]:
                scen = random.choice(SCENARIOS)
            else:
                print("\n")
                text_functions.print_slow(
                    "Choose a door between 1 and 3 (you idiot)")
                playloop(player)
            if scen == "Monster":
                monsterfight(player)
            if scen == "Treasure":
                open_chest(player)
            if scen == "Trap":
                trap(player)
    win_lose(player)


def win_lose(player):
    if player.HP == 0:
        text_functions.print_slow(
            "You died and lost the game. Better luck next time!")
        print("\n")
        print("\n")
        start()
    elif player.LVL == 10:
        text_functions.win_story()


text_functions.clear()
intro_music()
mixer.music.play(-1)
start()
