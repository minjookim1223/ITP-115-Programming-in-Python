# Minjoo Kim
# ITP 115, Fall 2019
# FINAL PROJECT - RESTAURANT SIMULATION
# minjook@usc.edu
# This file represents the class Diner. The class will perform basic functions such as updating diner's status

from MenuItem import MenuItem


class Diner(object):
    # class variable; static list to describe diner' status
    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]

    # instance variables to describe the diners
    def __init__(self, dinerName):  # take diner's name as an input
        self.name = dinerName       # assign the input in the name variable
        self.order = []             # assign order to an empty list
        self.status = 0             # start the diner's status at 0

    # Create getter/setter method for all of instance variables
    def getName(self):      # getter method for the name
        return self.name

    def setName(self, name):    # setter method for name
        self.name = name

    def getOrder(self, order):      # getter method for the order
        if order in self.order:
            return order

    def setOrder(self, order):      # setter method for the order
        self.order.append(order)

    def getStatus(self):            # getter method for the status
        return self.status

    def setStatus(self, status):    # setter method for the status
        self.status = status

    # method to update the status
    def updateStatus(self):
        self.status += 1    # update the status by 1

    # method to add the item in the order
    def addToOrder(self, menuItem):
        self.order.append(menuItem)     # append the menuItem object into diner's order list

    # method to print diner's order
    def printOrder(self):
        print("")                           # print a line to make it look pretty
        print(self.name, end="")            # print out diner's name, end with "" to make sure the code doesn't \n
        print(" ordered:")                  # print "ordered:"
        for k in range(len(self.order)):    # loop the list that contains diners' orders
            print("- ", end="")             # print the orders followed by -
            print(self.order[k])

    # calculate diner's meal cost when he/she is done with the food
    def calculateMealCost(self):
        mealCost = 0                            # the meal cost starts at 0
        for i in range(len(self.order)):        # loop the list of orders
            mealCost += float(self.order[i].price)  # add the cost of each menuItem one by one
        return mealCost                         # return the mealCost

    # message that is to be returned when printing the diner object
    def __str__(self):
        # store diner's current status in msg
        msg = "Diner " + self.name + " is currently " + Diner.STATUSES[self.status]
        return msg      # return msg
