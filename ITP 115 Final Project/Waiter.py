# Minjoo Kim
# ITP 115, Fall 2019
# FINAL PROJECT - RESTAURANT SIMULATION
# minjook@usc.edu

# This class will represent the waiter and his/her actions.

# import other files for their classes
from Menu import Menu
from Diner import Diner


# Initiate the Waiter class
class Waiter(object):
    # instance variables
    def __init__(self, menuObject):     # menuObject as input
        self.diners = []        # put list of diners into an empty list
        self.menu = menuObject  # set menu as the input

    # addDiner method
    # add each dinerObject into the instance variable list for diners
    def addDiner(self, dinerObject):
        self.diners.append(dinerObject)     # append dinerObject in self.diners list

    # method getNumDiners
    def getNumDiners(self):
        return len(self.diners)     # return the length of self.diners

    # method printDinerStatuses
    def printDinerStatuses(self):
        for i in range(len(Diner.STATUSES)):        # loop through possible diner's statuses from Diner's class variable
            print(Diner.STATUSES[i] + ": ")         # print a possible diner's status
            for j in range(len(self.diners)):       # and for each status, loop it so that you print the number of
                status = self.diners[j].status      # diners for that specific status
                if i == 0 and status == 0:          # ex) if i == 0 -> for each status, if j (diner's status) matches,
                    print("\t", end="")             # print them accordingly
                    print(self.diners[j])
                elif i == 1 and status == 1:
                    print("\t", end="")
                    print(self.diners[j])
                elif i == 2 and status == 2:
                    print("\t", end="")
                    print(self.diners[j])
                elif i == 3 and status == 3:
                    print("\t", end="")
                    print(self.diners[j])
                elif i == 4 and status == 4:
                    print("\t", end="")
                    print(self.diners[j])

    # method for taking orders
    def takeOrders(self):
        # get the number of each menuItems by categories
        # if there are 4 drinks for example, numDrinks should be 4
        numDrinks = self.menu.getNumMenuItemsByType("Drink")
        numAppetizer = self.menu.getNumMenuItemsByType("Appetizer")
        numEntree = self.menu.getNumMenuItemsByType("Entree")
        numDessert = self.menu.getNumMenuItemsByType("Dessert")

        # loop according to the number of diners
        for i in range(len(self.diners)):
            dinerStatus = self.diners[i].status  # dinerStatus = each diner's status
            if Diner.STATUSES[dinerStatus] == "ordering":   # if the diner's status is "ordering"
                self.menu.printMenuItemsByType("Drink")     # print the drink type
                print(self.diners[i].name + ", please select a Drink menu item number")     # ask the diner what drink
                keepAsking = True           # parameter for error checking loop
                while keepAsking:           # loop until keepAsking is False
                    drink = input()         # ask for diner's input for the drink
                    # if the input is a number & within correct range
                    if drink.isdigit():
                        if 0 <= int(drink) < numDrinks:
                            # add the chosen drink into diner's list of order
                            self.diners[i].addToOrder(self.menu.menuItemDrinkList[int(drink)])
                            # change the parameter to False so you get out of the loop
                            keepAsking = False

                # repeat the process above for appetizers
                self.menu.printMenuItemsByType("Appetizer")
                print(self.diners[i].name + ", please select a Appetizer menu item number")
                keepAsking = True
                while keepAsking:
                    appetizer = input()
                    if appetizer.isdigit():
                        if 0 <= int(appetizer) < numAppetizer:
                            self.diners[i].addToOrder(self.menu.menuItemAppetizerList[int(appetizer)])
                            keepAsking = False

                # repeat the process above for entrees
                self.menu.printMenuItemsByType("Entree")
                print(self.diners[i].name + ", please select a Entree menu item number")
                keepAsking = True
                while keepAsking:
                    entree = input()
                    if entree.isdigit():
                        if 0 <= int(entree) < numEntree:
                            self.diners[i].addToOrder(self.menu.menuItemEntreeList[int(entree)])
                            keepAsking = False

                # repeat the process above for desserts
                self.menu.printMenuItemsByType("Dessert")
                print(self.diners[i].name + ", please select a Dessert menu item number")
                keepAsking = True
                while keepAsking:
                    dessert = input()
                    if dessert.isdigit():
                        if 0 <= int(dessert) < numDessert:
                            self.diners[i].addToOrder(self.menu.menuItemDessertList[int(dessert)])
                            keepAsking = False

                # print the orders that the diners ordered previously
                self.diners[i].printOrder()

    # method to ring up diners
    # loop through the diners
    # if the diners are "paying"
    def ringUpDiner(self):
        for i in range(len(self.diners)):                               # loop it through the list of diners
            if Diner.STATUSES[self.diners[i].status] == "paying":       # if the diners are paying
                mealCost = self.diners[i].calculateMealCost()           # calculate the meal cost
                print("\n" + self.diners[i].name + ", your meal cost $" + str(mealCost))    # pring the meal cost

    # remove the diners method
    def removeDoneDiners(self):
        # loop through the list of diners
        for i in range(len(self.diners)):
            # if diners are leaving,
            # print out the message to send the customer off
            if Diner.STATUSES[self.diners[i].status] == "leaving":
                print("\n" + self.diners[i].name + ", thank you for dining with us! Come again soon!")
        # loop through the list backwards
        for i in range(len(self.diners)-1, -1, -1):
            # if the customer is leaving,
            if Diner.STATUSES[self.diners[i].status] == "leaving":
                del self.diners[i]      # delete the diner from the list of diners

    # advancing diners
    def advanceDiners(self):
        Waiter.printDinerStatuses(self)     # print diner's statuses
        Waiter.takeOrders(self)             # take orders
        Waiter.ringUpDiner(self)            # ring up diners
        Waiter.removeDoneDiners(self)       # remove diners when they are done
        for i in range(len(self.diners)):   # loop through the list of diners
            Diner.updateStatus(self.diners[i])  # update the diners' status every time by 1

