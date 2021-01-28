# Minjoo Kim
# ITP 115, Fall 2019
# Assignment #4 Part 2
# 9/29/2019
# minjook@usc.edu

# Description:
# This program simulates a dice game

import random


def main():

    score = 0

    for num in range(10):

        case = random.randrange(1, 6, 1)

        print("You are playing for CASE " + str(case))
        print("You will win for the following numbers: ")

        if case == 1:
            for i in range(1, 6, 1):
                print(str(i), end=" ")

        if case == 2:
            for i in range(1, 20, 2):
                print(str(i), end=" ")

        if case == 3:
            for i in range(5, 11, 1):
                print(str(i), end=" ")

        if case == 4:
            for i in range(10, 21, 2):
                print(str(i), end=" ")

        if case == 5:
            for i in range(3, 20, 3):
                print(str(i), end=" ")

        print("\n")

        print("Now rolling . . .")
        dice = random.randrange(1, 21, 1)
        print("You rolled a " + str(dice) + "!")

        win = False

        if case == 1:
            for i in range(1, 6, 1):
                if dice == i:
                    win = True

        elif case == 2:
            for i in range(1, 20, 2):
                if dice == i:
                    win = True

        elif case == 3:
            for i in range(5, 11, 1):
                if dice == i:
                    win = True

        elif case == 4:
            for i in range(10, 21, 2):
                if dice == i:
                    win = True

        elif case == 5:
            for i in range(3, 20, 3):
                if dice == i:
                    win = True

        if win:
            score = score + 50
            print("You won 50 points! :)")
        else:
            print("You didn't win :(")

        print("")

    print("Your total score is: " + str(score))
    print("Thanks for playing!")


main()
