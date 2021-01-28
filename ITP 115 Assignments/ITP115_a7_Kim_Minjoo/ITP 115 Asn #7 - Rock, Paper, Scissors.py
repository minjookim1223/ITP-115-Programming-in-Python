# Minjoo Kim
# ITP 115, Fall 2019
# Assignment #7
# 10/20/2019
# minjook@usc.edu

# Description:
# This program simulates rock, paper, scissors

import random

def main():
    repeat = True
    # count variables to keep track of how many times the player won, lost, and tied
    winCount = 0
    loseCount = 0
    tieCount = 0

    # while repeat is True (using continue function)
    while repeat:
        displayMenu()      # show the menu
        playerChoice = getPlayerChoice()    # accept player choice
        computerChoice = getComputerChoice()    # accept computer choice

        if playerChoice == 0:           # if the player chose rock
            print("You chose Rock.")    # print that he chose rock
            player = "Rock"             # make a variable for making printing easier later on
        elif playerChoice == 1:         # repeat this process for paper and scissors as well
            print("You chose Paper.")
            player = "Paper"
        elif playerChoice == 2:
            print("You chose Scissor.")
            player = "Scissors"

        if computerChoice == 0:     # do the same thing as above, but this time for computer choice
            print("Computer chose Rock.")
            computer = "Rock"
        elif computerChoice == 1:
            print("Computer chose Paper.")
            computer = "Paper"
        elif computerChoice == 2:
            print("Computer chose Scissor.")
            computer = "Scissors"

        win = playRound(computerChoice, playerChoice)   # determine who won through playRound function
        if win == 1:            # if player won
            winCount += 1       # add the winCount
            if playerChoice == 0:   # print how the player won for all options accordingly
                print("Rock smashes scissors.", end=" ")
            elif playerChoice == 1:         # if player chose paper
                print("Paper covers rock.", end=" ")
            elif playerChoice == 2:     # if player chose scissors
                print("Scissors cut paper.", end=" ")
            print("Player wins!")

        elif win == -1:     # if computer won
            loseCount += 1  # add the lostCount
            if computerChoice == 0:     # print how the computer won for all options accordingly
                print("Rock smashes scissors.", end=" ")
            elif computerChoice == 1:       # if computer chose paper
                print("Paper covers rock.", end=" ")
            elif computerChoice == 2:       # if computer chose scissors
                print("Scissors cut paper.", end=" ")
            print("Computer wins!")     # computer won

        elif win == 0:      # if they tied
            tieCount += 1   # add the tieCount
            print("It's a tie!")    #print that it's a tie

        repeat = continueGame()
        print("")

    print("You won " + str(winCount) + " game(s).")     # print out how many times the player won
    print("The computer won " + str(loseCount) + " games(s).")  # print out how many times the computer won
    print("You tied with the computer " + str(tieCount) + " times(s).") # print out how many ties there were
    print("")
    print("Thanks for playing!")


# display the menu
# print out all the instructions that were on the pdf file accordingly
def displayMenu():
    print("Welcome! Let's play rock, paper, scissors.")
    print("The rules of the game are:")
    print("\t Rock smashes scissors")
    print("\t Scissors cut paper")
    print("\t Paper covers rock")
    print("\t If both the choices are the same, it's a tie")


# get computer choice
def getComputerChoice():
    # 0 for rock, 1 for paper, 2 for scissors
    choiceList = [0, 1, 2]      # make a list for the choices
    return random.choice(choiceList)    # choose an option from the list at random


# get player's choice
# return an integer
def getPlayerChoice():
    choice = int(input("Please choose (0) for rock, (1) for paper or (2) for scissors\n"))
    return choice


# simulate the game by taking computer and player's choices
def playRound(computerChoice, playerChoice):
    if computerChoice == playerChoice:  # if they had the same chice
        return 0        # it was a tie

    elif computerChoice == 0:   # if computer chose rock
        if playerChoice == 1:   # if player chose paper
            return 1            # player won
        elif playerChoice == 2:  # if player chose scissors
            return -1           # computer won

    elif computerChoice == 1:   # if computer chose paper
        if playerChoice == 2:  # if player chose scissors
            return 1            # player won
        elif playerChoice == 0:  # if player chose rock
            return -1           # computer won

    elif computerChoice == 2:   # if computer chose scissors
        if playerChoice == 0:  # if player chose rock
            return 1        # player won
        elif playerChoice == 1:  # if player chose paper
            return -1       # computer won


# the return value will be the parameter for the loop
def continueGame():
    cont = input("Do you want to continue playing? Enter (y) for yes or (n) for no.\n") # based on what the user inputs
    if cont == "y":
        return True         # return True for y
    else:
        return False        # return False for n


main()
