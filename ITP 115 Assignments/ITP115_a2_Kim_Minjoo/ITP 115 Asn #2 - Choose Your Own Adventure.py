# Minjoo Kim
# ITP 115, Fall 2019
# Assignment #2 Part 2
# 9/15/2019
# minjook@usc.edu

# Description:
# This program simulates your own adventure at a local bar.


def main():
    print("Welcome to a choose your own adventure game.")

    print("School is over and it is time for you to meet your friends. Your friends told you if you can meet them at a local bar.")
    print("When you meet up with them, you see a cute girl.")

    # the first option
    print("Do you: ")
    print("a) You go up to her and introduce yourself")
    print("b) Start talking to your friends. She will introduce herself eventually")
    print("c) Start drinking. You didn't come here to meet girls")
    #prompt a choice
    choiceOne = input()

    # the first option leads to two choices
    if choiceOne == "a" or choiceOne == "A":
        print("You introduced yourself to her. You buy her a drink and have a nice chat.")
        print("Do you: ")
        print("a) Ask her on a date")
        print("b) Be a wingman for your friend. Your friend seems to like her.")
        # prompt the second choice
        choiceOneTwo = input()

        # scenarios based on choice two = A
        if choiceOneTwo == "a" or choiceOneTwo == "A":
            print("You ask her if she wants to have a dinner with you some time. She rejects you because she has a boyfriend. Better luck next time!")
        elif choiceOneTwo == "b" or choiceOneTwo == "B":
            print("You introduce her to your friend. Your friend asks her if she would be free for dinner some time. She rejects him because she has a boyfriend. Better luck next time!")
        else:
            print("You chose an invalid option. The story will choose a default option for you\n")
            print("You ask her if she wants to have a dinner with you some time. She rejects you because she has a boyfriend. Better luck next time!")

    # choices based on choice B
    elif choiceOne == "b" or choiceOne == "B":
        print("You talk to your friends. She doesn't even seem to notice you.")
        print("Do you: ")
        print("a) Decide to go and talk to her")
        print("b) Continue to pretend you don't see her at all")
        choiceOneTwo = input()

        if choiceOneTwo == "a" or choiceOneTwo == "A":
            print("You stand up from your seat and look for her. However, she already seems to be gone from the bar.")
        elif choiceOneTwo == "b" or choiceOneTwo == "B":
            print("You pretend not to see her. Who needs a girlfriend anyways?")
        else:
            print("You chose an invalid option. The story will choose a default option for you\n")
            print("You stand up from your seat and look for her. However, she already seems to be gone from the bar.")

    # choice c leads to...
    elif choiceOne == "c" or choiceOne == "C":
        print("You start drinking. You drink continuously for the next two hours. You get too drunk.")
        print("Do you: ")
        print("a) Not care about anything and start drinking")
        print("b) Talk to your friends that you don't need a girlfriend")
        choiceOneTwo = input()

        # scnearios based on your choice...
        if choiceOneTwo == "a" or choiceOneTwo == "A":
            print("You become intoxicated. Your friends call 911 and you are sent to the ER")
        elif choiceOneTwo == "b" or choiceOneTwo == "B":
            print("They say, \"Whatever you say\".")
        else:
            print("You chose an invalid option. The story will choose a default option for you\n")
            print("You become intoxicated. Your friends call 911 and you are sent to the ER")

    # invalid option: default back to choice one
    else:
        print("You chose an invalid option. The story will choose a default option for you\n")
        print("You start drinking. You drink continuously for the next two hours. You get too drunk.")
        print("Do you: ")
        print("a) Not care about anything and start drinking")
        print("b) Talk to your friends that you don't need a girlfriend")
        choiceOneTwo = input()

        if choiceOneTwo == "a" or choiceOneTwo == "A":
            print("You become intoxicated. Your friends call 911 and you are sent to the ER")
        elif choiceOneTwo == "b" or choiceOneTwo == "B":
            print("They say, \"Whatever you say\".")

    print("THE END")

main()