# Minjoo Kim
# ITP 115, Fall 2019
# Assignment #4 Part 1
# 9/29/2019
# minjook@usc.edu

# Description:
# This program calculates the character count for a given sentence.


def main():

    special = 0
    sentence = input("Please enter a sentence: ")

    print("special characters: ", end="")

    for letter in sentence:
        if ord(letter) > 32:
            if ord(letter) < 65 or ord(letter) > 122:
                special = special + 1

    if special == 0:
        print("NONE")

    elif special > 0:
        for num in range(special):
            print("*", end="")

    print("")

    for i in range(97, 123):
        count = 0
        print(chr(i) + ": ", end="")

        for letter in sentence:
            if letter == chr(i) or letter == chr(i-32):
                count = count + 1

        if count == 0:
            print("NONE")

        else:
            for j in range (count):
                print("*", end="")

            print("")


main()
