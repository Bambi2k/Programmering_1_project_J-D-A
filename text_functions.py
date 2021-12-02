import time
import sys
from pygame import mixer
import os


def outro():
    print_slow("Thank you for playing our game")
    print("\n")
    print_slow(
        "Coded by (in no specific order): Alexander Holmgren, Johan James and David Salomonsson")
    print("\n")
    print_slow("Main director: Alexander Holmgren")
    print("\n")
    print_slow("Executive producer: Johan James")
    print("\n")
    print_slow("Music design and story writer: David Salomonsson")
    print("\n")
    print_slow("Outside help: Martin Loman")
    print("\n")
    print_slow("Thank you again for playing. Hope you enjoyed it :)")
    print("\n")
    print_slow("Lots of love from BCAA STUDIOS")


def tutorial():
    print_slow("Welcome to our game! It is quite simple. You will follow a charachter that will explore multiple rooms, collecting items and treasure, fighting monsters and (hopefully not) dealing with traps")
    print("\n")
    time.sleep(1)
    print_slow("In each room you will be able to chose which action you want to execute. To open one of the doors: type open. To check stats: type stats. And if you want to check your bag: type bag")
    print("\n")
    time.sleep(1)
    print_slow(
        "The goal of the game is to get your LVL from 1 to 10, without dropping you HP below")
    print("\n")
    time.sleep(1)
    print_slow("A trap room will deal a random amount of damage to your HP capped at 3. The treasure rooms will have a item that you can bring along to boost your strength. You can carry 5 items at a time. Lastly the monster room, where you will fight a monster with a random strength. If you have more strength than the monster, you win and gain 1 LVL while if you have less strength than the monster, you lose and forfeit 1 HP  ")
    print("\n")
    time.sleep(1)
    print_slow("Pretty simple huh? Lets get this going shall we?")
    print("\n")
    time.sleep(2)
    print("\n\n")


def intro():
    print("\n")
    print_slow("Darkness")
    # time.sleep(1)
    print("\n")
    print_slow("Nothing but darkness")
    # time.sleep(1)
    print("\n")
    print_slow(
        "You feel around you with your hands, struggling to understand what is going on")
    # time.sleep(1)
    print("\n")
    print_slow("The ground is cold to the touch")
    # time.sleep(1)
    print("\n")
    print_slow("You stand up and reach for your phone")
    # time.sleep(1)
    print("\n")
    print_slow("No cell connection...")
    # time.sleep(1)
    print("\n")
    print_slow("You turn on the flashlight and look around")
    # time.sleep(1)
    print("\n")
    print_slow("I gotta get out of here")
    # time.sleep(1)
    print("\n")
    # time.sleep(2)
    print_slow("Walking a couple of meters reveales 3 identical doors.")
    print("\n")
    time.sleep(1)
    mixer.music.fadeout(6000)
    time.sleep(6)


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0)
        # times.sleep(0.05)

# Bokstav för bokstav print men något snabbare än den ovan


def win_story():
    print_slow("You reached lvl 10!")
    time.sleep(1)
    print("\n")
    print_slow("You look around in the darkness")
    time.sleep(1)
    print("\n")
    print_slow(
        "Silhouttes of the monsters you have slain laying on the ice cold floor")
    time.sleep(1)
    print("\n")
    print_slow("You hear footseps approaching your room.")
    time.sleep(1)
    print("\n")
    print_slow(
        "You hear the wooden door creak as light floods your room from the outside")
    time.sleep(1)
    print("\n")
    print_slow("A beam of light, bright as the sun flickers to life above you")
    time.sleep(1)
    print("\n")
    print_slow(
        "'George?! What are you doing up so late?' you hear a familiar voice say")
    time.sleep(1)
    print("\n")
    print_slow(
        "'Uhhh... Nothing mom. Just cleaning my room' you respond instinctively")
    time.sleep(1)
    print("\n")
    print_slow(
        "'Well you did not do a very good job then. Go to bed NOW!' she said strictly")
    time.sleep(1)
    print("\n")
    print_slow("'Alright mom' you answer.")
    time.sleep(1)
    print("\n")
    print_slow("As you stand up and look around, you see your monster stuffed animals laying on the ground. Next to you is a foam sword")
    time.sleep(1)
    print("\n")
    print_slow("'I wish I could keep playing' I said to myself")
    time.sleep(1)
    print("\n")
    print_slow("The light turns of as you curl up in your bed")
    time.sleep(1)
    print("\n")
    print_slow("THE END")
    print("\n")
    print("\n")
    time.sleep(6)
    outro()


def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
