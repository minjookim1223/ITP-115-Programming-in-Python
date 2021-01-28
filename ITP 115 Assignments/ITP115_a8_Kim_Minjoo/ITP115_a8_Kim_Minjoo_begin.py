# Minjoo Kim
# ITP 115, Fall 2019
# Assignment #8
# 11/03/2019
# minjook@usc.edu

# Description:
# This program simulates Tic, Tac, Toe

import TicTacToeHelper


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


def playGame():
    # initializing the board with an empty list, then filling it out with 0 - 8
    boardList = []
    for i in range(9):
        boardList.append(i)
    # created to keep track of turns
    turnCount = 0
    # variable to keep track of whose turn it is
    player = "x"
    # variable to account for while loop
    result = "n"

    print("Welcome to Tic Tac Toe!")
    printPrettyBoard(boardList)

    while result == "n":
        valid = False
        while not valid:
            spot = int(input("Player " + player + " , pick a spot: "))
            valid = isValidMove(boardList, spot)
            if valid:
                updateBoard(boardList, spot, player)
                turnCount += 1
                # if it was x's turn, now it's going to be o's turn
                if player == "x":
                    player = "o"
                elif player == "o":
                    player = "x"
                printPrettyBoard(boardList)
            else:
                print("Invalid move, please try again.")

        whoWon = TicTacToeHelper.checkForWinner(boardList, turnCount)
        if whoWon == "x" or whoWon == "s" or whoWon == "o":
            result = True
            print("")
            print("Game over!")
            if whoWon == "x" or whoWon == "o":
                print("Player " + whoWon + " is the winner!")
            elif whoWon == "s":
                print("Stalemate reached!")


def main():
    playAgain = True
    while playAgain:
        playGame()
        playAgain = input("Would you like to play another round? (y/n): ")
        if playAgain == "y":
            playAgain = True
        elif playAgain == "n":
            playAgain = False
        else:
            print("Invalid input. The game will end.")
            playAgain = False

    print("Goodbye!")


main()
