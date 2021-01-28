# Minjoo Kim
# ITP 115, Fall 2019
# Assignment #10
# 11/17/2019
# minjook@usc.edu

# Description:
# This program simulates animal daycare using OOP


class Animal(object):
    # create all the class attributes
    # with all the inputs as necessary
    # all the inputs are assigned to the attributes
    def __init__(self, hunger, happiness, health, energy, age, name, species):
        self.hunger = hunger
        self.happiness = happiness
        self.health = health
        self.energy = energy
        self.age = age
        self.name = name
        self.species = species

    # class method play
    def play(self):
        # add 10 to happiness
        # if happiness is 100+,
        # set happiness to 100
        self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100

        # increase hunger by 5
        # if hunger is more than 100,
        # set hunger to 100
        self.hunger += 5
        if self.hunger > 100:
            self.hunger = 100

    # feed method
    # reduce hunger by 10
    # if hunger is less 0, set it to 0
    def feed(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0

    # giveMedicine method
    # reduce happiness by 20
    # if happiness is less than 0, set it to 0
    def giveMedicine(self):
        self.happiness -= 20
        if self.happiness < 0:
            self.happiness = 0

        # increase health by 20
        # if health is bigger than 100, set it to 100
        self.health += 20
        if self.health > 100:
            self.health = 100

    # sleep method
    def sleep(self):
        # increase energy by 20
        # if energy is > 100, set it to 100
        self.energy += 20
        if self.energy > 100:
            self.energy = 100

        # you age 1 every time you sleep
        self.age += 1

    # __str__ function.
    # print each animal's status in pretty
    # return status
    def __str__(self):
        status = "Name: " + str(self.name) + " the " + str(self.species) + "\n" + "Health: " + str(self.health) + (
                 "\n" + "Happiness: " + str(self.happiness) + "\n" + "Hunger: " + str(self.hunger) + "\n") + (
                 "Energy: " + str(self.energy) + "\n" + "Age: " + str(self.age))
        return status


# loadAnimals function with input of a csv file
# load animals in a list and return the list
def loadAnimals(csvTitle):
    # create an animalList to include all the animal objects
    animalList = []

    # open the file
    fileIn = open(csvTitle, "r")
    # loop through each line
    # we have to create an animal object for each line
    for line in fileIn:
        # strip the spaces at the beginning and end of all the strings
        line = line.strip()
        # split the lines; take out ","
        dataList = line.split(",")

        # create an animal object with each data in a line as inputs
        animal = Animal(int(dataList[0]), int(dataList[1]), int(dataList[2]), int(dataList[3]), int(dataList[4]),
                        dataList[5], dataList[6])
        # append the animal object in the list
        animalList.append(animal)

    # close the file to keep the file from getting corrupt
    fileIn.close()
    # return the animalList
    return animalList


# function to display the menu
# print all the options that the user can take
def displayMenu():
    print("1) Play")
    print("2) Feed")
    print("3) Give Medicine")
    print("4) Sleep")
    print("5) Print an Animal's stats")
    print("6) View All Animals")
    print("7) Exit\n")


# selectAnimal function
# allows the user to select an animal to treat after choosing an option from the displayMenu
def selectAnimal(animalList):
    # print each the name each animal by going through the animalList using for loop
    # loop it based on the number of animals in the list
    for i in range(len(animalList)):
        print(str(i+1) + ") " + animalList[i].name + " the " + animalList[i].species)

    # print a line to make it pretty
    print("")

    # valid is the parameter to use the while loop
    # error checking
    select = 0
    valid = False
    while not valid:
        # ask the user to pick an animal
        select = input("Please select an animal from the list (enter 1-5): ")
        # if the number is a digit and anywhere from 1-5
        if select.isdigit() and 0 < int(select) < 6:
            # the input is valid
            valid = True
            # else, try again
        else:
            print("*Invalid input, please try again!\n")

    # return select
    return select


def saveFile(animalList):
    fileOut = open("animals.csv", "w")
    for i in range(5):
        # strip the spaces at the beginning and end of all the strings
        print(animalList[i].hunger, end=",", file=fileOut)
        print(animalList[i].happiness, end=",", file=fileOut)
        print(animalList[i].health, end=",", file=fileOut)
        print(animalList[i].energy, end=",", file=fileOut)
        print(animalList[i].age, end=",", file=fileOut)
        print(animalList[i].name, end=",", file=fileOut)
        if i == 4:
            print(animalList[i].species, end="", file=fileOut)
        else:
            print(animalList[i].species, file=fileOut)

    # close the file to keep the file from getting corrupt
    fileOut.close()


# the main function
def main():

    # load the animal using loadAnimals def
    animalList = loadAnimals("animals.csv")

    # parameter to play the game
    select = "0"

    # while loop to play the game and repeat the menu choosing process
    # if the user chooses option 7, quit
    while int(select) != 7:
        # valid to be used as a parameter for displaying the menu
        valid = False
        # while not valid,
        while not valid:
            # display the menu
            displayMenu()
            # ask the user for an option
            select = input("Please make a selection: ")

            # error checking for the first menu
            if select.isdigit() and 0 < int(select) < 8:
                valid = True
            else:
                print("*Invalid selection, please try again.\n")

        # if the user chooses 1,
        if int(select) == 1:
            # choose the animal to play with
            animal = int(selectAnimal(animalList))
            # play with the animal by calling the play method
            animalList[animal-1].play()
            # print out which animal you played with
            print("You played with " + animalList[animal - 1].name + " the " + (
                animalList[animal - 1].species) + "!\n")

        # if the user chooses 2,
        if int(select) == 2:
            # have the user choose the animal to feed
            animal = int(selectAnimal(animalList))
            # feed the animal by calling the feed method
            animalList[animal-1].feed()
            # print out which animal you fed
            print("You fed " + animalList[animal - 1].name + " the " + (
                animalList[animal - 1].species) + "!\n")

        # if the user chose 3
        if int(select) == 3:
            # choose the animal to give medicine
            animal = int(selectAnimal(animalList))
            # give the medicine
            animalList[animal-1].giveMedicine()
            # show that you fed the medicine
            print("You gave " + animalList[animal - 1].name + " the " + (
                animalList[animal - 1].species) + " some medicine!\n")

        # if the user chose 4,
        if int(select) == 4:
            # choose the animal to have it nap
            animal = int(selectAnimal(animalList))
            # make the animal sleep
            animalList[animal-1].sleep()
            # tell the user that it took a nap
            print(animalList[animal - 1].name + " the " + (
                animalList[animal - 1].species) + " took a nap!\n")

        # if the user chose 5,
        if int(select) == 5:
            # choose the animal to show its status
            animal = int(selectAnimal(animalList))
            # print the status
            print(animalList[animal-1])
            # print a nice little line to separate the status from the next option/menu/etc.
            print("********************************\n")

        # if the menu is 6, then print all of animal's info
        if int(select) == 6:
            for i in range(len(animalList)):
                print(animalList[i])
                # print a nice little line to separate the status from the next option/menu/etc.
                print("********************************")
            print("")

    # if the user chooses 7, the game is done
    # save the file
    saveFile(animalList)

    print("Goodbye!")


main()
