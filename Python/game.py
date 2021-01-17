import random
import sys

ans = ""
coat = False
flare = False
machete = False
again = True
# Possible areas go here:
def cave():
    print("You head towards the cave")
    print("you reach the cave and find a corpse of an animal nearby")
    ans = input("Do you A) continue into the cave for the night or B) turn around and head for the jungle? ")
    if ans.lower() == "a":
        print("You head into the cave")
        print("You settle into the cave and decide to build a fire with some sticks")
        print("Upon starting the fire you fall asleep next to it")
        print("You wake up a little while later with a Panther starting at you")
        ans = input("Do you A) jump up in fear or B) slowly get up and walk out of the cave slowly ")
        if ans.lower() == "a":
            print("You jump up rapily scaring the Panther who runs off and you decide to leave the cave and start your day")
            print("You see A) the jungle and B) the beach where you woke-up")
            ans = input("Where do you go? ")
            if ans.lower() == "a":
                print("You head for the Jungle")
            elif ans.lower() == "b":
                print("You head for the Beach")
            else:
                print("Invalid input you died")
                death()
        elif ans.lower() == "b":
            print("You get up slowly and the Panther approches you as you try to leave")
            print("the Panther then pounces and mauls you")
            print("You died :(")
        else:
            print("Invalid input you died from animal mauling")
            death()
def jungle():
    print("You head towards the jungle")
    print("You find A) a old tree-house just inside the jungle and B) a you see a small village off in the distance")
    ans = input("Where do you go? ")
    if ans.lower() == "a":
        print("You go to the tree-house")
        print("You find a ladder leading up to the tree-house")
        print("You reach the top and climb inside to find an older man sleeping")
        print("You wake the man up and you have a conversation about being stuck on the island")
        print("Turns out he has a radio and can get a boat to get you off the island")
        print("You catch the boat and made it Home! Congrats!")
        death()
    elif ans.lower() == "b":
       village()
    else:
        print("Invalid input you died")
        death()
        
def plane():
    print("You go towards the plane crash")
    print("You reach the plane crash and find a coat and a flare")
    coat = True
    flare = True
    ans = input("You see a A) cave and a B) jungle near by where do you go? ")
    if ans.lower() == "a":
        cave()
    elif ans.lower() == "b":
        jungle()
    else:
        print("Invalid input you died")
        

def beach():
    print("You reach the beach and find a various assortment of driftwood and palm trees")
    ans = input("Do you A) Attempt to build a raft, or B) build a giant help sign ")
    if ans.lower() == "a":
        print("You remeber as a child you watch survivor and know how to make string from palm leaves")
        print("You spend the next few days drinking coconuts and building the raft")
        if flare:
            print("As you set off on the raft you see a ship in the distance")
            print("youse use the flare you found to alert them and then sail out to them")
            print("Congrats you survived!")
            death()
            
        else:
            print("You set off on the raft with a set of coconuts hoping to find a way back to civilization")
            random.seed()
            chance = random.randint(1, 2)
            if(chance == 1):
                print("You end up starving to death after many days at sea")
                print("You died! Try again!")
                death()
                
            elif(chance == 2):
                print("After many days at sea you spot land off in the distance")
                print("You reached civilization and survived! Congrats!")
                death()
                

def palmTrees():
    print("You reach the palm trees")
    print("After walking through groups of Palms for awhile you find a hidden grove")
    print("Inside the grove is a beautiful assortment of tropical fruit trees and a fresh spring of water")
    ans = input("Do you A) trust this magical place and stay for awhile, B) Leave the place and head for the jungle nearby, or C) Head back for the plane crash ")
    if ans.lower() == "a":
        magicalPlace()
    elif ans.lower() == "b":
        jungle()
    elif ans.lower() == "c":
        plane()
    else:
        print("Invalid input you died")
        death()
        
def luggage():
    print("You go towards the luggage")
    print("Once there you find some useful items")
    print("You found a flare and a coat and a machete")
    machete = True
    flare = True
    coat = True
    ans = input("From here you see a A) jungle, B) plane crash, C) small Village ")
    if ans.lower() == "a":
        jungle()
    elif ans.lower() == "b":
        plane()
    elif ans.lower() == "c":
        village()
    else:
        print("Invalid input you died")
        death()
    
def magicalPlace():
    print("You decide to stay")
    print("Once you start eating the fruit you forget all about being on a deserted island")
    print("You fashion a small house out of palm trees and leaves and decide to stay here for the rest of your life")
    print("You didn't die but also didn't make it off the island. You Survived (kind of)!")
    death()
    
def village():
    print("You go towards the village")
    print("You reach the village and a group of children come out to meet you")
    print("They start dancing and chanting around you. You get an uneasy feeling")
    ans = input("Do you A) stay in the village or B) run for the beach down the coast ")
    if ans.lower() == "a":
        print("You choose to stay and the children lead you to the main house")
        print("When you reach the house someone comes up behind you and knocks you out")
        print("You awake tied up over a fire. The village people are cannibals!")
        print("You were made into food and died")
        input("Better luck next time! ")
        death()
    elif ans.lower() == "b":
        print("You take off running down the coast and the people start chasing you")
        print("You finally get away and head slowly to the beach")
        beach()
    else:
        print("Invalid input you died")
        death()
        
def death():
    ans = input("Would you like to play again? Y/N ")
    if ans.lower() == "y":
        again = True
    else:
        again = False
        input("Thanks for Playing!!")
        sys.exit()


# Start of main code
while(again):
    if(again == False):
        exit
    print("Welcome to the text based make your own story game!")
    print("You wake up with nothing on a deserted island and you look around")
    print("You see A) a plane crash B) a group of palm trees in the distance C) a small pile of luggage from the plane crash.")
    ans = input("Where would you like to go? ")   
    if ans.lower() == "a":
        plane()
    elif ans.lower() == "b":
        print("You head for the palm trees")
        palmTrees()
    elif ans.lower() == "c":
        luggage()
    else:
        print("Invalid input you died")
        death()
exit