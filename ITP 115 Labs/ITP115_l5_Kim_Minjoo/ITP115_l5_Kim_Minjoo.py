# Minjoo Kim
# ITP 115, Fall 2019
# Lab 5
# minjook@usc.edu

import random   # importing "random" for the sentence generator


def main():

    # tentative lists for articles, nouns, and verbs
    articles = ["a", "the"]
    nouns = ["person", "place", "thing"]
    verbs = ["danced", "ate", "frolicked"]
    choice = "1"  # choice for the menu

    # Loop until the user wants to quit
    while choice != "5":

        # print out the menu
        print("Welcome to the Sentence Generator")
        print("Menu")
        print("1) View Words")
        print("2) Add words")
        print("3) Remove Words")
        print("4) Generate Sentence")
        print("5) Exit")

        # enter your option (put in string because it would make an error for any int options
        choice = input()

        # choice 1
        if choice == "1":
            # print out all the lists
            print(articles)
            print(nouns)
            print(verbs)
            print("")

        # choice 2
        elif choice == "2":
            # prompt the user to choose what to add (noun or verb)
            userInput = input("Enter 1) for nouns or 2) for verbs: ")

            # prompt the user to add a noun
            if userInput == "1":
                noun = input("Enter the word: ")
                # add a noun to the noun list
                nouns.append(noun)
                print("")

            # prompt the user to add a verb
            elif userInput == "2":
                verb = input("Enter the word: ")
                # add a verb to the verb list
                verbs.append(verb)
                print("")

            # if there is a wrong option, exit. ask the a new option
            else:
                print("Option not listed")

        # choice 3; removing a noun or a verb
        elif choice == "3":
            # prompt the user to choose what to remove
            userInput = input("Enter 1) for nouns or 2) 2 verbs: ")

            # prompt the user to enter a noun
            if userInput == "1":
                noun = input("Enter the word: ")

                # if the noun is found, then remove
                if noun in nouns:
                    nouns.remove(noun)
                    print("")

                # if noun is not found, then cancel
                else:
                    print("Word not in list\n")

            # prompt the user to enter a verb
            elif userInput == "2":
                verb = input("Enter the word: ")

                # if the verb is found, then remove
                if verb in verbs:
                    verbs.remove(verb)
                    print("")

                # else, cancel
                else:
                    print("Word not in list\n")

            # if the user does not choose between verb or a noun, then cancel
            else:
                print("Option not listed")

        # choice 4
        elif choice == "4":
            # print out an article, noun, verb, article, then a noun
            print(random.choice(articles), random.choice(nouns), random.choice(verbs), random.choice(articles), random.choice(nouns) + "\n")

        # choice 5, exit
        elif choice == "5":
            print("Program will exit")
            print("Have a great day!")

        # wrong choice; go back to the menu
        else:
            print("Invalid choice.\n")


main()
