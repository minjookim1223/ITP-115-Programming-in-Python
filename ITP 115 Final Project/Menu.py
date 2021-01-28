# Minjoo Kim
# ITP 115, Fall 2019
# FINAL PROJECT - RESTAURANT SIMULATION
# minjook@usc.edu
# Menu Class
# This class represents the restaurant's menu which contains four different
#       menu items diner can order from

# import MenuItem class from the file MenuItem
from MenuItem import MenuItem


class Menu(object):
    # static list to describe each type of menuItem
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    def __init__(self, csvMenuFile):
        self.menuItemDrinkList = []         # list containing all the DRINK menu items from menu
        self.menuItemAppetizerList = []     # list containing all the APPETIZER menu items from menu
        self.menuItemEntreeList = []        # list containing all the ENTREE menu items from menu
        self.menuItemDessertList = []       # list containing all the DESSERT menu items from menu

        fileIn = open(csvMenuFile, "r")         # read the file
        for line in fileIn:                 # for each line in the file
            line = line.strip()                     # strip and get rid of commas
            dataList = line.split(",")              # put it in the list by splitting (delimiter of ",")

            # create MenuItem object based on information from each line
            menuObject = MenuItem(dataList[0], dataList[1], dataList[2], dataList[3])

            # insert the menuObject in one of the menuItem___List based on its type compared to the strings
            #       that are within the static variable MENU_ITEM_TYPES
            if dataList[1] == Menu.MENU_ITEM_TYPES[0]:
                self.menuItemDrinkList.append(menuObject)
            elif dataList[1] == Menu.MENU_ITEM_TYPES[1]:
                self.menuItemAppetizerList.append(menuObject)
            elif dataList[1] == Menu.MENU_ITEM_TYPES[2]:
                self.menuItemEntreeList.append(menuObject)
            elif dataList[1] == Menu.MENU_ITEM_TYPES[3]:
                self.menuItemDessertList.append(menuObject)

        # close the file to prevent any file corruption
        fileIn.close()

    # Get the correct MenuItem from the lists using its type and index position in the list of items
    def getMenuItem(self, itemType, itemIndex):     # itemType and itemIndex as inputs
        if itemType == Menu.MENU_ITEM_TYPES[0]:                 # if the itemType and menu's item type are equal
            if itemIndex <= len(self.menuItemDrinkList)-1:      # put it in the drink list
                return self.menuItemDrinkList[itemIndex]
        elif itemType == Menu.MENU_ITEM_TYPES[1]:               # do the same comparison
            if itemIndex <= len(self.menuItemAppetizerList)-1:  # put it in the appetizer list
                return self.menuItemAppetizerList[itemIndex]
        elif itemType == Menu.MENU_ITEM_TYPES[2]:               # same comparison
            if itemIndex <= len(self.menuItemEntreeList)-1:     # put it in the entree list
                return self.menuItemEntreeList[itemIndex]
        elif itemType == Menu.MENU_ITEM_TYPES[3]:               # same comparison
            if itemIndex <= len(self.menuItemDessertList)-1:    # put it in the dessert list
                return self.menuItemDessertList[itemIndex]      # make sure to check whether the index is okay

    # print menu items by type
    # to be implemented in Waiter class
    def printMenuItemsByType(self, itemType):       # take itemType as an input (one of the food categories)
        if itemType == Menu.MENU_ITEM_TYPES[0]:     # if the itemType input matches one of the categories,
            print("\n-----Drinks-----")             # print out the Drinks (header)
            for j in range(len(self.menuItemDrinkList)):    # use for loop to go through the drink list
                print(str(j) + ") " + self.menuItemDrinkList[j].name + "(" + self.menuItemDrinkList[
                    j].type + "): $" + self.menuItemDrinkList[j].price)     # format it correctly to make it look pretty
                print("\t" + self.menuItemDrinkList[j].description)         # include all the instance variables of the
                                                                            # drink objects

        # continue to do the same thing for all the other categories (appetizers, entrees, and desserts)
        elif itemType == Menu.MENU_ITEM_TYPES[1]:
            print("\n-----Appetizers-----")
            for j in range(len(self.menuItemAppetizerList)):
                print(str(j) + ") " + self.menuItemAppetizerList[j].name + "(" + self.menuItemAppetizerList[
                    j].type + "): $" + self.menuItemDrinkList[j].price)
                print("\t" + self.menuItemAppetizerList[j].description)

        # continue for entree
        elif itemType == Menu.MENU_ITEM_TYPES[2]:
            print("\n-----Entrees-----")
            for j in range(len(self.menuItemEntreeList)):
                print(str(j) + ") " + self.menuItemEntreeList[j].name + "(" + self.menuItemEntreeList[
                    j].type + "): $" + self.menuItemEntreeList[j].price)
                print("\t" + self.menuItemEntreeList[j].description)

        # do the same for dessert
        elif itemType == Menu.MENU_ITEM_TYPES[3]:
            print("\n-----Desserts-----")
            for j in range(len(self.menuItemDessertList)):
                print(str(j) + ") " + self.menuItemDessertList[j].name + "(" + self.menuItemDessertList[
                    j].type + "): $" + self.menuItemDessertList[j].price)
                print("\t" + self.menuItemDessertList[j].description)

    # return the integer representing number of MenuItems of the input type
    # if there are four drink objects in the list above, then it will return the integer 4
    def getNumMenuItemsByType(self, itemType):  # use itemType as an input
        if itemType == Menu.MENU_ITEM_TYPES[0]:     # if the type matches one of the categories,
            return len(self.menuItemDrinkList)      # return the length of the list
        elif itemType == Menu.MENU_ITEM_TYPES[1]:   # repeat for all other categories
            return len(self.menuItemAppetizerList)
        elif itemType == Menu.MENU_ITEM_TYPES[2]:
            return len(self.menuItemEntreeList)
        elif itemType == Menu.MENU_ITEM_TYPES[3]:
            return len(self.menuItemDessertList)


