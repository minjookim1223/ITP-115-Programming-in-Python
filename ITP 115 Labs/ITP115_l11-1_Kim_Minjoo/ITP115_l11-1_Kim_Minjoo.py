# Minjoo Kim
# ITP 115, Fall 2019
# L11-1
# minjook@usc.edu

# This program simulates a rolling of two dice and finding the sum of the values based on user input

import random


# Die class
class Die(object):
    # Instance attributes with variables rollValue and sides
    def __init__(self, numSides):
        self.sides = numSides
        self.rollValue = 0

    # change the rollValue to anywhere from 1 - how many sides there are
    def roll(self):
        self.rollValue = random.randrange(1, self.sides+1)

    # __str__ for printing later based on die's info
    def __str__(self):
        dieInfo = "Die has " + str(self.sides) + " sides and " + "rolled a " + str(self.rollValue)
        return dieInfo


# calculate die1 and die2's values and add them up.
def calculateSum(die1, die2):
    die1.roll()     # roll the first die
    print(die1)     # print the value

    die2.roll()     # repeat for the second die
    print(die2)

    total = die1.rollValue + die2.rollValue     # add the values
    return total        # and return the value


def main():
    # ask whether the user wants to use the default number of sides or not
    firstDecision = input("Use the default number of sides for first die(y/n)? ")
    if firstDecision == "y":        # if yes,
        firstSides = 6              # default side = 6
    elif firstDecision == "n":      # if not,
        firstSides = int(input("How many sides? "))     # ask how many sides they want
    else:
        print("Wrong input. Will use 6 sides")      # if they don't put y or n, use the default number
        firstSides = 6

    # repeat the same process for the second die
    secondDecision = input("Use the default number of sides for second die(y/n)? ")
    if secondDecision == "y":
        secondSides = 6
    elif secondDecision == "n":
        secondSides = int(input("How many sides? "))
    else:
        print("Wrong input. Will use 6 sides")
        secondSides = 6

    # ask how many rolls they want
    numRolls = int(input("How many times do you want to roll the die? "))

    # create objects for both dies
    dieOne = Die(firstSides)
    dieTwo = Die(secondSides)

    # implement calculateSum function by passing die objects
    for i in range(numRolls):
        total = calculateSum(dieOne, dieTwo)
        # print out the sum
        print("The sum of Dice 1 and Dice 2 is " + str(total))


main()

