"""
Richie Doherty
"""

import random
name = input("What is your name? \n>")
print("Hello " + name + " are you a Warrior, Wizard or a Programmer?")
title = input("Warrior, Wizard or a Programmer? (Spelling Matters)\n>")
fname = title +' ' + name

name_len = len(fname)

if name_len <= 15:
    print(".xX WELCOME " + fname + " Xx.")

else:
    print("Welcome " + title)

if title == "Programmer":
    print("There is no treasure here for you. The real treasure is the time spent programming.")

if title != "Warrior" and title != "Wizard" and title != "Programmer":
    print("Come back when you have a real job or can learn to follow instructions!")

if title == "Warrior" or title == "Wizard":
    print("You are in a glass room, with a door that leads to a long hallway,"
          "The room is completely empty.... except for a chest!")
    chest = input("Would you like to open the chest or leave it? \n>")
    if chest == "Open" or chest == "open":
        open = random.randint(1,21)
        print(open)
        if open <= 5:
            print("OH NO! The glass is cracking!")
        elif open >= 6 and open <= 10:
            print("You got a bottle of windex")
        elif open >=11 and open <= 15:
            print("You received a rubix cube, play away!")
        elif open >+ 16:
            print("You received the key! You are free to go")
    elif chest == "Leave" or chest == "leave":
        print("Nothing happened, you are stuck like Magneto")
    else:
        print("You didn't follow instructions! Game Over")



