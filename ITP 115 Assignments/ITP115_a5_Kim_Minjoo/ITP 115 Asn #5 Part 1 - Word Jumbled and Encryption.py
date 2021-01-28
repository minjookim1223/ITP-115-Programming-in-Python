# Minjoo Kim
# ITP 115, Fall 2019
# Assignment #5 Part 1
# 10/06/2019
# minjook@usc.edu

# Description:
# This program simulates a word jumble game

import random


def main():
    # the list of all the words
    words = ["bottle", "python", "peacock", "elephant", "crocodile"]

    # list of hints
    hints = ["Contains water", "Snakes?", "Flash bird", "Trunk", "Reptile"]

    # randomly choose a word for the player to guess
    word = random.choice(words)

    # return the index of the word chosen
    wordIndex = words.index(word)

    # put the alphabets in a list
    wordList = list(word)

    # choose a random alphabet; swap with the current index
    for i in range(0, len(word), 1):
        temp = random.choice(wordList)
        tempIndex = wordList.index(temp)
        wordList[tempIndex] = wordList[i]
        wordList[i] = temp

    # a variable to store the jumbled word
    jumbled = "".join(wordList)

    # variable to store how many tries it took
    count = 0

    # Give user the question
    print("The jumbled word is", "\"" + jumbled + "\"")

    # checks whether the player used a hint or not
    usedHint = False

    # If correct is true, then stop the loop.
    correct = False
    while not correct:
        # keeping track of how many guesses
        count += 1

        # enter your guess
        guess = input("Please enter your guess: ")

        # checking if the player's guess is correct
        if guess == word:
            print("You got it!")
            if count == 1:
                print("It took you 1 try.")
            else:
                print("It took you " + str(count) + " tries.")

                # awarding based on points
                if not usedHint:
                    print("You didn't use the hint. 10 points for you!")
                else:
                    print("You used the hint. 5 points for you!")

            correct = True
        else:
            print("Try again.")

        # prompting hints if more than 3 tries, assuming that the player didn't use the hint and didn't get the answer
        if count > 2 and usedHint == False and correct == False:
            hint = input("Would you like a hint? [y/n]: ")  # ask if they want a hint
            if hint == "y":  # if yes,
                print("Hint:", hints[wordIndex])  # print out the hint based on the index
                usedHint = True  # used the hint
            elif hint == "n":  # if not, NVM
                print("Nvm!")
            else:  # typed something wrong
                print("Sorry, I didn't get that.")


main()
