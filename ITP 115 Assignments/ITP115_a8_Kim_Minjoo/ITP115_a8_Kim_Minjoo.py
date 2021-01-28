# Minjoo Kim
# ITP 115, Fall 2019
# Assignment #8
# 11/03/2019
# minjook@usc.edu

# Description:
# This program simulates Tic, Tac, Toe

import TicTacToeHelper
import random


def isValidMove(boardList, spot):
    # check if spot is within 0 ~ 8
    if 0 <= spot <= 8:
        # check if there is x or o in here
        if boardList[spot] != "x" and boardList[spot] != "o":
            # if yes, return True
            return True
            # otherwise, return False
        else:
            return False
    # else, return False
    else:
        return False

# update the board based on given spot and player's symbol
def updateBoard(boardList, spot, playerLetter):
    # at the spot in the boardList, draw playerLetter
    boardList[spot] = playerLetter


# print the pretty board
def printPrettyBoard(boardList):
    print()
    # since the input is only the board, we have to make a separate counter
    # to print each spot one by one
    counter = 0
    # 2-D array
    # for each column
    for i in range(3):
        # for each row
        for j in range(3):
            # print | after each number in a row
            if j == 0 or j == 1:
                print(boardList[counter], end=" | ")
                # add the counter to print the next number in the boardList
                counter += 1
            # don't print | after the last number in each row
            else:
                print(boardList[counter])
                counter += 1
        # print ------- for the first and the second row
        if i == 0 or i == 1:
            print("---------")

#
def playGame():
    # initializing the board with an empty list, then filling it out with 0 - 8
    # created boardList to keep track of the current board
    boardList = []
    # created tempList to limit what the computer can choose later for its move
    tempList = []
    for i in range(9):
        boardList.append(i)
        tempList.append(i)
    # created to keep track of turns
    turnCount = 0
    # variable to keep track of whose turn it is
    turn = "x"
    # variable to account for while loop
    result = "n"

    # greeting
    print("Welcome to Tic Tac Toe!")
    # print the board
    printPrettyBoard(boardList)

    # ask the player whether he/she wants to play against the computer.
    computerOption = input("Would you like to play against the computer? (y/n): ")
    # if yes,
    if computerOption == "y":
        # ask the player whether he/she wants to go first or not
        player = input("Which symbol do you want to choose (x/o): ")
        # if yes, computer goes second
        if player == "x":
            computer = "o"
        # if no, computer goes first
        elif player == "o":
            computer = "x"
        # if the player's input is invalid, he/she will go first.
        else:
            print("Invalid option.")
            print("You will play as x")
            player = "x"
            computer = "o"
    # if the player doesn't want to play against the computer
    elif computerOption == "n":
        # we don't need the variable
        computer = ""
    # if the player doesn't know/enter wrong input
    else:
        # player doesn't play against the computer
        print("Invalid option. You won't be playing against the computer")
        computerOption = "n"
        computer = ""
    # while there is not conclusion in the game
    while result == "n":
        # to check the validity of the move
        valid = False
        # if the move is not valid:
        while not valid:
            # IF THE USER IS PLAYING AGAINST ANOTHER USER
            if computerOption == "n":
                # each player picks a spot
                spot = int(input("Player " + turn + ", pick a spot: "))
                # use isValidMove to check the validity of the move
                valid = isValidMove(boardList, spot)
                # if it is valid, update the board
                if valid:
                    updateBoard(boardList, spot, turn)
                    turnCount += 1
                    # if it was x's turn, now it's going to be o's turn
                    if turn == "x":
                        turn = "o"
                    elif turn == "o":
                        turn = "x"

                    # print the board
                    printPrettyBoard(boardList)
                # if the move is not valid, try again
                else:
                    print("Invalid move, please try again.")

            # if the player wants to play against the computer,
            if computerOption == "y":
                # if it's the player's turn
                if turn == player:
                    # the player chooses a spot to draw his/her symbol
                    spot = int(input("Player " + turn + ", pick a spot: "))
                    # check if the move is valid,
                    valid = isValidMove(boardList, spot)
                    # if his/her move is valid,
                    if valid:
                        # update the board
                        updateBoard(boardList, spot, player)
                        turnCount += 1
                        # remove that spot from the tempList to limit what the computer can choose later
                        tempList.remove(spot)
                        # print the board
                        printPrettyBoard(boardList)
                        # switch turns
                        if turn == "x":
                            turn = "o"
                        elif turn == "o":
                            turn = "x"
                    # if the move is invalid,
                    else:
                        # try again
                        print("Invalid move, please try again.")

                # if it's computer's turn,
                elif turn == computer:
                    # choose a spot from tempList in random based on what is there left
                    spot = random.choice(tempList)

                    valid = isValidMove(boardList, spot)
                    if valid:
                        updateBoard(boardList, spot, computer)
                        turnCount += 1
                        print("Computer took its move")
                        printPrettyBoard(boardList)
                        tempList.remove(spot)
                        if turn == "x":
                            turn = "o"
                        elif turn == "o":
                            turn = "x"
                    #else:
                    #    print("Invalid move, please try again.")

        whoWon = TicTacToeHelper.checkForWinner(boardList, turnCount)
        if whoWon == "x" or whoWon == "s" or whoWon == "o":
            result = True
            print("")
            print("Game over!")
            if whoWon == "x" or whoWon == "o":
                print("Player " + whoWon + " is the winner!")
            elif whoWon == "s":
                print("Stalemate reached!")


# main to actually call playGame()
def main():
    # parameter to loop
    playAgain = True
    # while the player wants to play the game,
    while playAgain:
        # play the game
        playGame()
        # when the game is done, ask the player if he/she wants to play again
        playAgain = input("Would you like to play another round? (y/n): ")
        # if yes, keep playAgain as True
        if playAgain == "y":
            playAgain = True
        # if not, false,
        elif playAgain == "n":
            playAgain = False
        # if there is an invalid input, end the game.
        else:
            print("Invalid input. The game will end.")
            playAgain = False

    print("Goodbye!")


# call the main
main()
