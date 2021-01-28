# Minjoo Kim
# ITP 115, Fall 2019
# Assignment #6
# 12/06/2019
# minjook@usc.edu

# Description:
# This program simulates an automated airplane reservation system

# plane't TOTAL capacity
TOTAL_SEATS = 10


# a function for assigning seats
# takes number of seats filled and the list of the seating as inputs
def assignSeats(numFilledSeats, seatMap):
    if numFilledSeats < 10:                             # assuming the seats are not booked fully,
        name = input("Please enter your first name: ")  # take in the customer's name
        seatMap.append(name)                            # append the name in the list of seats
    else:
        print("The plane is overbooked!")               # otherwise, state that the seats are overbooked


# a function for printing the seats
def printSeatMap(numFilledSeats, seatMap):
    print("***************************************")
    for i in range(TOTAL_SEATS):                         # loop it through the maximum amount of seats
        print("\t  Seat #" + str(i+1) + ":", end="")     # format it so that it prints "Seat #:
        if i < numFilledSeats:                           # afterwards, according to the number of filled seats,
            print("\t  " + seatMap[i])                   # print the names of the ones who booked the seats
        else:                                            # else,
            print("\t  Empty")                           # print that it's empty
    print("***************************************\n")


# print the boarding pass based on name or seat number
def printBoardingPass(numFilledSeats, seatMap):
    # give the user the option of searching for the boarding pass based on seat number of name
    option = input("Type 1 to get Boarding Pass by seat number\nType 2 to get Boarding Pass by name\n")

    # find the boarding pass by seat number
    if option.isdigit() and int(option) == 1:               # error checking: make sure whether the input is a int(1)
        seat = input("What is the seat number: ")           # ask for the seat number
        if seat.isdigit() and int(seat) <= numFilledSeats:  # error checking for the seat number
            print("\n======= BOARDING PASS =======")        # print out the boarding pass
            print("\tSeat #:", seat)
            print("\tPassenger Name:", seatMap[int(seat)-1])    # account for the list's index
            print("=============================")              # the list's index starts from 0, so make sure to
            print("")                                           # subtract 1 from the seat number that the user gives
        else:
            print("Invalid number--no boarding pass found\n")   # if the number was not found, print the error msg

    # find the boarding pass by name
    elif option.isdigit() and option == "2":                # error checking: check if the option is int(2)
        name = input("Enter passenger name: ")              # ask for the passenger's name
        if name in seatMap:                                 # if the name is in the list,
            seatIndex = seatMap.index(name)                 # return the seatIndex based on where the name is located
            print("\n======= BOARDING PASS =======")        # print the boarding pass
            print("\tSeat #: ", seatIndex + 1)              # seat number is seat's index + 1 since the list starts at 0
            print("\tPassenger Name: ", seatMap[seatIndex])     # find the passenger's name in the seatMap
            print("=============================")
        else:
            print("No passenger with name " + name + " was found\n")    # otherwise, print our an error msg

    else:
        print("Invalid input. Try again.")      # error msg for invalid input


def main():
    choice = "1"                # parameter for inputs
    valid = choice.isdigit()    # to check whether the choice is valid
    seatMap = []                # the list that will be used to store seat data
    numFilledSeats = 0          # number of seats filled thus far

    while choice != "-1":           # while the choice is not -1 (since -1 is used to quit)
        if valid and 1 <= int(choice) <= 3:     # print out the menu ony when choice is from 1 - 3
            print("1:\tAssign Seat.")
            print("2:\tPrint Seat Map.")
            print("3:\tPrint Boarding Pass.")
            print("-1:\tQuit.\n")

        choice = input()        # accept user's input

        # the variable "valid" is used for error checking (check above; used to see if the choice is int)
        if valid and int(choice) == 1:              # if the input is 1,
            assignSeats(numFilledSeats, seatMap)    # use assignSeats to assign the seats
            if numFilledSeats < TOTAL_SEATS:        # assuming the seats are not overbooked,
                numFilledSeats += 1                     # add the filled seats by 1

        elif valid and int(choice) == 2:            # if the user chooses number 2
            printSeatMap(numFilledSeats, seatMap)   # print the seatMap

        elif valid and int(choice) == 3:                # if the user chooses 3,
            printBoardingPass(numFilledSeats, seatMap)  # print the appropriate boarding pass

        elif choice == "-1":              # if the user chooses -1,
            break                         # exit the loop

        else:           # wrong input results in this msg rather reiterating the menu
            print("Please enter choice: ", end="")

    print("Have a nice day!")


main()


