# Minjoo Kim
# ITP 115, Fall 2019
# Assignment #5 Part 2
# 10/06/2019
# minjook@usc.edu

# Description:
# This program simulates word encryption/decryption (not considering capital letters)


def main():

    # a list of alphabets
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

    # list to put the shifted alphabets
    shifted = []

    # prompt the user to enter a message
    message = input("Enter a message: ")

    # make the message into a list
    messageList = list(message)

    # enter how much to shift the alphabets by
    shift = int(input("Enter a number to shift by (0-25): "))

    # make a list of shifted alphabets
    for i in range(0, 26, 1):
        place = i + shift
        if place >= 26:     # if the list goes over 26,
            place = place-26    # come back to the start of the alphabet

        shifted.append(alphabets[place])    # add the alphabets one by one into a list

    # ENCRYPTING
    print("Encrypting message....")

    for i in range(len(message)):       # for the length of the message
        index = 0       # keep the index
        found = False      # a parameter to prevent non-alphabets from changing
        for j in range(26):     # check all 26 alphabets
            if messageList[i] == alphabets[j]:  # if an alphabet is found
                index = j       # return that index
                found = True    # found the alphabet
        if found:               # if found,
            messageList[i] = shifted[index]     # use that index to get the shifted alphabet

    encrypted = "".join(messageList)        # join the chars in the list

    print("     Encrypted message: " + encrypted)    # print the encrypted message

    # DECRYPTING
    print("Decrypting message....")

    for i in range(len(message)):   # essentially the same process except
        index = 0
        found = False
        for j in range(26):
            if messageList[i] == shifted[j]:    # check if the alphabet in the message matches the shifted alphabet
                index = j
                found = True
        if found:
            messageList[i] = alphabets[index]   # and return the actual alphabet's value based on that index

    decrypted = "".join(messageList)    # join it in decrypted message

    print("     Decrypted message: " + decrypted)    # print the decrypted message

    # Original message
    print("     Original Message:", message)


main()
