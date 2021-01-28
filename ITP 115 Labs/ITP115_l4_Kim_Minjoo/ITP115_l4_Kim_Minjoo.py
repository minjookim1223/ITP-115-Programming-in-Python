# Minjoo Kim
# ITP 115, Fall 2019
# Lab 4
# minjook@usc.edu

# if the word is three letters or fewer, append "en" to the end of the word
# if the word is four letters or more, append a random vowel to the end of the word
# Change all c's to k's using a for loop

import random


def main():

    lists = ["a", "e", "i", "o", "u"]       # list of vowels
    repeat = "y"        # condition for keeping the loop

    print("Welkomeo Toen theen Pigen Elvisha Translatore!")     # intro
    print("(Welcome to the Pig Elvish translator!)\n")

    while repeat == "y":

        word = input("Please enter a word you would like to translate: ")   # translate
        translate = word

        if len(word) <= 4:          # if the word is longer than 4 letters, put en
            translate = translate + "en"

        else:
            translate = translate + random.choice(lists)        # else, append a random vowel

        translated = ""     # replace c with k
        for letter in translate:
            if letter == "c":
                translated = translated + "k"
            else:
                translated = translated + letter

        print(translated)
        print("\n")

        repeat = input("Would you like to translate another word? (y/n): ")

        print("\n")

    print("Goodbyea! Havea aen nicee dayen!")


main()