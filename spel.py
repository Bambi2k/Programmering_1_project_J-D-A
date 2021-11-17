# Här inför vi några moduler som vi behöver för koden
import time
import sys
import random as rand

# De tre olika scenarios som kan förekomma när man öppnar dörrarna
scenarios = ["Monster", "Trap", "Treasure"]

# Karaktärens väska eller inventory i början av spelet
bag = []

# Karaktärens basvärden
HP = 10
STR = 5
LVL = 1

# Functionen som startar igång spelet


def start():
    play = input(
        "Would you like to start the game? (yes/no): ").lower().strip()
    if play == "yes":
        want_tutorial = input(
            "Would you like a tuturial? (Yes/No): ").lower().strip()
        if want_tutorial == "yes":
            tutorial()
        elif want_tutorial == "no":
            intro()
    elif play == "no":
        print_slow("Maybe next time")
    elif play != "yes" or "no":
        again1()

# Förklaring till hur spelet fungerar och spelas


def tutorial():
    print_medium("Welcome to our game! It is quite simple. You will follow a charachter that will explore multiple rooms, collecting items and treasure, fighting monsters and (hopefully not) dealing with traps")
    print()
    time.sleep(1)
    print_medium("In each room you will be able to chose which action you want to execute. To open one of the doors: type open. To check stats: type stats. And if you want to check your bag: type bag")
    print()
    time.sleep(1)
    print_medium(
        "The goal of the game is to get your LVL from 1 to 10, without dropping you HP below")
    print()
    time.sleep(1)
    print_medium("A trap room will deal a random amount of damage to your HP capped at 3. The treasure rooms will have a item that you can bring along to boost your strength. You can carry 5 items at a time. Lastly the monster room, where you will fight a monster with a random strength. If you have more strength than the monster, you win and gain 1 LVL while if you have less strength than the monster, you lose and forfeit 1 HP  ")
    print()
    time.sleep(1)
    print_medium("Pretty simple huh? Lets get this going shall we?")
    print()
    time.sleep(2)
    print()
    print()
    intro()

# Spelets loop som kör igenom spelet.


def playloop():
    while HP >= 0 or LVL <= 10:
        print_slow("What would you like to do?")
        print()
        choice = input(
            "Would you like to: open a door, check stats or check inventory? ").lower().strip()
        if choice == "bag":
            print_slow("Your bag contents: ", bag)
        if choice == "stats":
            print_slow("Your stats; HP:", HP, "STR:", STR, "LVL:", LVL)


# Skapar lite klar yta i termninalen
def clear():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()

# ifall ett alternativ som inte finns skrivs in (eller en felstavning), så skicker denna tillbaks dig till frågan


def again1():
    time.sleep(1)
    print_slow("Please enter a valid answer")
    clear()
    start()

# Bokstav för bokstav print, för en mer långsam och förstårbar upplevelse


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

# Bokstav för bokstav print men något snabbare än den ovan


def print_medium(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)


# Sätter stämmngingen för spelet och introducerar var vår karaktär är någonstans
def intro():
    print()
    print_slow("Darkness")
    time.sleep(1)
    print()
    print_slow("Nothing but darkness")
    time.sleep(1)
    print()
    print_slow(
        "You feel around you with your hands, struggling to understand what is going on")
    time.sleep(1)
    print()
    print_slow("The ground is cold to the touch")
    time.sleep(1)
    print()
    print_slow("You stand up and reach for your phone")
    time.sleep(1)
    print()
    print_slow("No cell connection...")
    time.sleep(1)
    print()
    print_slow("You turn on the flashlight and look around")
    time.sleep(1)
    print()
    print_slow("I gotta get out of here")
    time.sleep(1)
    print()
    time.sleep(2)
    print_slow("Walking a couple of meters reveales 3 identical doors.")
    print()
    time.sleep(1)
    playloop()


clear()
start()
