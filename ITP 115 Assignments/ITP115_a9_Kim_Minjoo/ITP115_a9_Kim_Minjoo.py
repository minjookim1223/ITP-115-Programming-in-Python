# Minjoo Kim
# ITP 115, Fall 2019
# Assignment #9 - File Processing
# 11/10/2019
# minjook@usc.edu

# Description:
# This program finds cars with the best and worst MPG (city)


def main():
    # print the greeting
    print("Welcome to EPA Mileage Calculator")
    # initialize the year
    year = 0
    # Ask which year the user wants to see
    # If the year is not 2009 or 2009, repeat
    while year > 2009 or year < 2008:
        year = int(input("What year would you like to view data for? (2008 or 2009): "))
        # repeat, but make sure to print out the error statement
        if year > 2009 or year < 2008:
            print("*Invalid input, please try again!")

    # maximum and minimum will be used to compare the mileage values
    maximum = 0
    minimum = 100000000000
    # maxCars and minCars will be used to keep the names of the cars with max/min mileages
    maxCars = []
    minCars = []

    # create the fileName we want based on the year that the user wants to see
    fileName = "epaVehicleData" + str(year) + ".csv"

    # read the file
    fileIn = open(fileName, "r")
    # the first line is used as a header
    headerLine = fileIn.readline()

    # read the file line by line using for loop
    for line in fileIn:
        # strip the spaces at the beginning and end of all the strings
        line = line.strip()
        # split the lines; take out ","
        dataList = line.split(",")
        # make sure to get the full car name by combining the car make and model
        carName = dataList[1] + " " + dataList[2]
        # make sure to keep vans, minivans and trucks out of the question by
        # using .find method.
        # If find returns -1 (if these categories are not found)
        if dataList[0].find("van") < 0 or dataList[0].find("minivan") < 0 or dataList[0].find("truck") < 0:
            # check if the current mileage is bigger than the "maximum"
            if int(dataList[8]) > maximum:
                # if it is, you have a new maximum
                maximum = int(dataList[8])
                # make sure to clear maxCars so that you can put your new model into the list
                maxCars.clear()
                # enter the new car name into the list
                maxCars.append(carName)

            # if the current mileage actually equates to the current maximum
            # also, make sure you are not repeating the car name
            if int(dataList[8]) == maximum and carName not in maxCars:
                # no need to change the mileage, but add to the maxCars list
                maxCars.append(dataList[1] + " " + dataList[2])

            # same logic follows for minimum
            # if the current city mileage is less than minimum
            if int(dataList[8]) < minimum:
                # you have a new minimum!
                minimum = int(dataList[8])
                # if so, make sure to clear the minCars list
                minCars.clear()
                # make sure to append the new carName for minimum mileages
                minCars.append(carName)

            # if the current mileage actually equates to the current minimum
            # also, make sure you are not repeating the car name
            if int(dataList[8]) == minimum and carName not in minCars:
                # make sure to append the new carName for minimum mileages
                minCars.append(carName)

    # close the file to avoid any file corruption
    fileIn.close()

    # ask for a new name of the file to write these results
    resultFile = input("Enter the filename to save results to: ")
    # open the file for writing
    fileOut = open(resultFile, "w")

    # Beginning format for the new file
    print("EPA City MPG Calculator", year, file=fileOut)
    print("----------------------------", file=fileOut)

    # Write all the info we got
    # Start with the maximum city mileage
    print("Maximum Mileage (city):", str(maximum), file=fileOut)
    # iterate all the elements in maxCars
    for i in range(len(maxCars)):
        print("\t", maxCars[i], file=fileOut)

    # Next, provide the user with the minimum mileage
    print("Minimum Mileage (city):", str(minimum), file=fileOut)
    # iterate all the elements in minCars
    for i in range(len(minCars)):
        print("\t", minCars[i], file=fileOut)

    # close the file to avoid any file corruption
    fileOut.close()

    # All of the processes are done.
    print("Operation Success! Mileage data has been saved to " + resultFile)
    print("Thanks, and have a great day!")


main()
