# Kumar Goodwin-Kennedy and Connie Cheng
# When sci-fi and ancient warriors collide you get an epic adventure. Enter the future as a skilled warrior of your choosing. You'll find yourself abord a mysterious alien ship. Can you find your way back home or fall to the creatures only thought of as myth.

# importing random number generator from random
from random import randint

# choose character function, prompts user to pick a character option and calls background function
def choose_character():
    character= input("Some people only get to read about legends. You get to live as one. \n Are you a ninja, a samurai, a knight or a mage?\n")
    if character == "ninja":
        print("You will live the legend of the stealthy ninja, Hayabusa.")
    elif character == "samurai":
        print("You will live the legend of the stealthy samarai, Jack.")
    elif character == "knight":
        print("You wil live the legend of the royal knight, Arthur.")
    elif character == "mage":
        print("You will live the legend of the majestic mage, Merlin.")
    else:
        print("Not an option bucko, pick one of the above!")
        choose_character()
    background()

# displays background text and calls choices function
def background():
    print("""You're enjoying the battle fueled atmosphere that is around you right now.\nThe sound of war can be heard throughout the land. \nAs you're running towards your next opponent a portal opens and you fall in. """)
    choices()

# display left or right options to navigate
def choices():
    print("""You awake in a daze to find yourself laying on a cold metal floor in a dark room. \nAfter looking around the room you notice a window and two doors. \nWhen you look into the window all you can see is the eternal darkness of the void known as space. \nWhile being in such a confused state you decide to go through one of the doors to figure out where you are. \n""")
    # prompts user for choice input and provides options to follow response
    door_choice= input("Do you go left or right? ")
    if door_choice== "left":
        slime_trail()
    elif door_choice== "right": 
        print("You hear a growling noise. You reach for your weapon and swing.")
        attack()
    else:
        print("Pick left or right!")
        choices()
        
def slime_trail():
    choose_slime=input("You see a something glimmer in the corner above you. On the floor you see a slime trail stretching into the darkness, do you follow it or go up?")
    # prompts user for choice input and provides options to follow response
    if choose_slime == "follow" or "yes":
        print("You find an injured slime alien.")
        print("The alien attacks you!")    
        attack()
    elif choose_slime =="up":
        print("Genius! You found an air duct and crawl through it.")
        print("You fall out into the engine room.")
        air_duct()
    else:
        print("Choose up or follow ")
        slime_trail()

def air_duct():
    air_duct_choice= input("You're stuck at a cross roads, do you go left or right? ")
    if air_duct_choice=="right":
        engine_room()
    elif air_duct_choice =="left":
        print("You hear a whirring noise and stumble on a trip laser.")
        # call die function ends game
        die()
    else:
        print("Not the time for that now!")
        air_duct()

def engine_room():
    print("You see all sorts of alien gadgetry.")
    print("And in the corner, a portal!")
    print("In the other corner is a shiny door.")
    final_choice= input("Do you go through the door or the portal? ")
    if final_choice=="portal":
        good_end()
    elif final_choice=="door":
        print("As soon as you reach the door, an alarm starts blaring.")
        print("The alien guards swarm in and take you to be dissected. \n")
        # call die function ends game
        die()    
    else:
        print("Now's not the time for that.\n")
        engine_room()

def attack():
    swing = randint(0,10)
    if swing <= 4:
        print("You miss and fall. Before you black out you feel the alien's teeth digging in your neck. ")
        # call die function ends game
        die()
    else:
        print("You manage to land a hit, as the alien shrieks you barrel past it.")
        escape()

def escape():
    print("You keep running forward but you feel more lost than when you started. You are at an intersection")
    fork_choice=input("Do you go left, right, forward? ")
    if fork_choice=="left":
        print("You walk into a room with other beings trapped in green tubes. You hear a noise behind you.")
        # call die function ends game
        die()
    elif fork_choice=="right":
        print("Something about this place feels familiar...")
        # restart at choice function
        choices()
    elif fork_choice=="forward":
        # call engine_room function
        engine_room()
    else:
        # toss user into edge case
        really_bad_choice()


def good_end():
    # ends game
    print("""Congratulations you have made it back to your time period, but why do the aliens continue to travel to your era...........""")
    start_over=input("Play again? ")
    # provide user option to restart game
    if start_over == "y" or "yes" or "Y" or "Yes":
        choose_character()
    else:
        return

def die():
    print("Better luck next time")
    start_over=input("Play again? ")
    # provide user option to restart game
    if start_over == "y" or "yes" or "Y" or "Yes":
        choose_character()
    else:
        return

def really_bad_choice():
    print("You fall into a hole")
    i=0
    while(i<1000000):
        print("That keeps going...")
        i+=1
    print("Then you die")
    # call die function ends game
    die()

# starts game
choose_character()