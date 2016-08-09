#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports

from sys import exit
from sys import argv

# Body


def infinite_stairway_room(count=0):
    print("Now {}, You walk through the door to see a dimly lit hallway.".format(argv[1]))
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light or take the back room door')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print('You take the stairs')
        if (count > 0):
            print("but you're not happy about it")
        infinite_stairway_room(count + 1)
    # option 2 == ?????
    if "door" in next:
        back_room()

def back_room():
    print("This room is full of awesome programmers.If you want to stay, state your name or choose another door")
    next = input(">")

    if 'door' not in next:
        print("Welcome {}!".format(next))
        dead("{}, You soon start programming and now love python so much that you don't want to leave ".format(sys.argv[1]))
        
    else:
        main()


def gold_room():
    print("Hey {}, This room is full of gold.  How much do you take?".format(argv[1]))

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice {}, you're not greedy, you win!".format(argv[1]))
        exit(0)
    else:
        dead("{}, You greedy goose!".format(argv[1]))


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if "take" in next or "honey" in next:
            dead("The bear looks at you then slaps your face off.")
        elif "taunt" in next and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif "taunt" in next and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif "open" in next or "door" in next and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Now {}, Here you see the great evil Cthulhu.".format(argv[1]))
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    next = input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    #user_name = sys.argv[1]
    print("Hi {} !, Welcome to text adventure".format(argv[1]))
    print("You are in a dark room.")
    print("There is a door to your right, left and front of you.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    elif "front" in next:
        infinite_stairway_room()
    else:
        dead("You stumble around the room until you starve.")

if __name__ == '__main__':
    main()
