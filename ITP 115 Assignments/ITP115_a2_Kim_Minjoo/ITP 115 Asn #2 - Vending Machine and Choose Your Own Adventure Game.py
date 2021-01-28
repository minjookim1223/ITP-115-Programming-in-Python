# Minjoo Kim
# ITP 115, Fall 2019
# Assignment #2 Part 1
# 9/15/2019
# minjook@usc.edu

# Description:
# This program simulates the vending machine system based on Harry Potter currency

def main():

    # the following items are all calculated in knuts
    correct = False

    print("Please Select an item from the vending machine:")
    while correct == False:   # looping for any errors until correct is True
        print("     a) Butterbeer: 58 knuts") #print out the options a - d
        print("     b) Quill: 10 knuts")
        print("     c) The Daily Prophet: 7 knuts")
        print("     d) Book of Spells: 400 knuts")

        choice = input()    # this is for what you are buying
        if choice == "a" or choice == "A":  # account for capital letter errors
            item = "Butterbeer"     # set up the item
            cost = 58       # set the cost
            correct = True  # choose the condition to get out of the loop
        elif choice == "b" or choice == "B":
            choice = "Quill"
            cost = 10
            correct = True
        elif choice == "c" or choice == "C":
            choice = "The Daily Prophet"
            cost = 7
            correct = True
        elif choice == "d" or choice == "D":
            choice = "Book of Spells"
            cost = 400
            correct = True
        else:
            print("You have entered an invalid option. Please choose again: ")  # ask again.

    instagram = input("Will you share this on Instagram? (y/n): ")      # post on instagram?

    if instagram == "y" or instagram == "Y":    # yes, then discount = 5
        discount = 5
    elif instagram == "n" or instagram == "N":      # no, then discount = 0
        discount = 0
    else:
        print("You have entered an invalid option. No coupon will be used.\n")      # invalid option. no discount
        discount = 0

    galleon = int(input("How many galleons would you like to pay?: "))
    sickle = int(input("How many sickles would you like to pay?: "))
    knut = int(input("How many knuts would you like to pay?: "))

    payment = galleon * 493 + sickle * 29 + knut

    print("You bought a " + choice + " for " + str(cost) + " knuts (with coupon of " + str(discount) + " knuts) and paid " + str(galleon) + " galleons, " + str(sickle) + " sickles, " + str(knut) + " knuts.")

    cost = cost - discount      # the actual final cost
    change = payment - cost     # change in knuts

    print("Here is your change (" + str(change) + " knuts):")

    sickleChange = change // 29     # how many sickles you get
    knutChange = change % 29    # how many knuts you get

    print("Sickles: " + str(sickleChange))
    print("Knuts: " + str(knutChange))


main()