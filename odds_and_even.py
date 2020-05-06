"""
Richie Doherty
"""

print("Let's play even and odds")
#importing random module for the computer input
import random

#start infinite loop
test = True

#infinite loop
while test == True:

    #User Input
    answer = input("Would you like to be odds or evens?")

    #End infinite loop if user correct answer
    if answer == 'evens' or answer == 'odds':
        test = False

#User input for series win critera
win = int(input("How many wins do you want to set to win the game? \n>"))

#Testing User input
if win < 1:
    print("No one wins, game over!")
else:
    print("Okay, " + str(win) + " wins will win the game!")

#Start game
#If series isn't greater than 1 game is not played
if win > 0:
    print("Lets play odds and evens")
    print()

# Setting scores
    player_score = 0
    com_score = 0
    round = 1

#Starting loop of game
    while player_score <= win or com_score <= win:
        #Printing top of score card every round
        print(str(win) + " will win the game.")
        print("Round " + str(round))
        print("=" * 5)
        print("Number of wins")
        print("Player:" + str(player_score) + ", Computer: " + str(com_score))
        print()

        #User input
        user = int(input("How many fingers will you play? (1 or 2)"))

        #test user input
        if user != 1 and user != 2:
            #if not 1 or 2 skips round
            continue
        #Generate computer play
        com_play = random.randint(1,2)

        #Testing game logic
        if user == 1 and com_play == 1:
            print("Player played" + " ☝️ " + str(user))
            print("Computer played" + " ☝️ " + str(1))
            print("Total is 2: Even")
            if answer == "evens":
                print("Player Wins Round " + str(round))
                print()
                player_score += 1
            else:
                print("Computer Wins Round " + str(round))
                print()
                com_score += 1
        if user == 2 and com_play == 2:
            print("Player played" + " ✌️ " + str(user))
            print("Computer played" + " ✌️ " + str(2))
            print("Total is 4: Even")
            if answer == "evens":
                print("Player Wins Round " + str(round))
                print()
                player_score += 1
            else:
                print("Computer Wins Round" + str(round))
                print()
                com_score += 1

        if user == 1 and com_play == 2:
            print("Player played" + " ☝️ " + str(user))
            print("Computer played" + " ✌️ " + str(2))
            print("Total is 3: odd")
            if answer == "odds":
                print("Player Wins Round " + str(round))
                print()
                player_score += 1
            else:
                print("Computer Wins Round " + str(round))
                print()
                com_score += 1

        if user == 2 and com_play == 1:
            print("Player played" + "️ ✌️ " + str(user))
            print("Computer played" + " ☝️ " + str(1))
            print("Total is 3: odd")
            if answer == "odds":
                print("Player Wins Round " + str(round))
                print()
                player_score += 1
            else:
                print("Computer Wins Round " + str(round))
                print()
                com_score += 1

        #Adds to round total
        round += 1

#Final win determinationt
        if player_score >= win:
            print()
            print("PLAYER WINS THE GAME! " + str(player_score) + " to " + str(com_score))
            #end while loop
            break
        elif com_score >= win:
            print()
            print("COMPUTER WINS THE GAME! " + str(com_score) + " to " + str(player_score))
            #end while loop
            break