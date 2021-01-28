# Minjoo Kim
# ITP 115, Fall 2019
# L9-1
# minjook@usc.edu

# This program simulates a coin flipping

import random


# simulates the coin flipping
def coin():
    output = ["heads", "tails"]     # make a list of heads and tail
    return random.choice(output)    # flip the coin out using random


# call coin() to flip the coin
# check how many times it would take for your to get 3 heads in a row
def experiment():
    countHeads = 0  # variable to count if you get three heads in a row
    countTotal = 0  # variable to count the total number of flips it took
#   used flipList to check out if the function was working correctly
    #   flipList = []

    while countHeads < 3:   # loop until you get three heads in a row
        flip = coin()       # call coin() to flip the coin
        #        flipList.append(flip)      used this to visualize if the function was working correctly
        countTotal += 1     # add to the number of flips
        if flip == "heads":     # if you et a head, add to countHeads variable
            countHeads += 1
        else:       # else, countHeads = 0; start over to get three heads in a row
            countHeads = 0

#    print(flipList)     # again, I used flipList to visualize what is going on
    return countTotal   # return the number of flips it took to get 3 consecutive heads


def main():
    flipCount = 0       # tentative variable to divide by 10 in order to get the average of 10 flips
    for i in range(10):     # loop the flips 10 times
        flips = experiment()    # calling experiment() to perform the flips and get the total flips to get 3 heads
        flipCount += flips      # add the flipCount variable

    flipAverage = flipCount / 10.0      # divide by 10.0 to get the average
    print("The average for 3 heads in a row is: " + str(flipAverage))       # print out the result


main()
