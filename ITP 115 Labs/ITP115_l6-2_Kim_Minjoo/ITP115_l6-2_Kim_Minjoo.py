# Minjoo Kim
# ITP 115, Fall 2019
# L6-2
# minjook@usc.edu


def main():

    # ask for the user's input
    sentence = input("Please enter a sentence (including numbers): ")

    # make a list for the input
    sentenceList = list(sentence)

    # make lists to store indices for digits and alphas
    digitList = []
    alphaList = []

    # use a for loop to store the indices into the lists created above
    for i in range(0, len(sentence), 1):
        if sentenceList[i].isalpha():
            alphaList.append(i)
        if sentenceList[i].isdigit():
            digitList.append(i)

    print("Here is the sentence breakdown:\n")

    # if the list is empty, there's NONE
    print("LETTERS:")
    if not alphaList:
        print("NONE\n")

    else:
        # check if the sentenceList[i] is an alphabet. If so, print -. Otherwise, print the number.
        for i in range(len(sentence)):
            if sentenceList[i].isalpha():
                print("-", end="")
            else:
                print(sentenceList[i], end="")
        print("")
        print("Letters occur at the following positions:")
        # print the digits indices stored
        for i in range(len(alphaList)):
            print(alphaList[i], end=" ")

        print("\n")

    # if the list is empty, there's NONE
    print("NUMBERS:")
    if not digitList:
        print("NONE")
    else:
        # check if the sentenceList[i] is a number. If so, print -. Otherwise, print the original
        for i in range(len(sentenceList)):
            if sentenceList[i].isdigit():
                print("-", end="")
            else:
                print(sentenceList[i], end="")
        print("")
        # print the indices stored.
        print("Numbers occur at the following positions:")
        for i in range(len(digitList)):
            print(digitList[i], end=" ")

main()
