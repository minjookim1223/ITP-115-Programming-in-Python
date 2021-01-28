# Minjoo Kim
# ITP 115, Fall 2019
# FINAL PROJECT - RESTAURANT SIMULATION
# minjook@usc.edu
# menuItem class. This class represents a single item that a diner can order from the menu


# Initiate the MenuItem class
class MenuItem(object):
    # instance variables with four inputs
    def __init__(self, name, itemType, price, description):
        self.name = name                # name of the menuItem
        self.type = itemType            # string representing the type of item
        self.price = price              # price of the item
        self.description = description  # a description of the item

    # Getter and setters for all the attributes
    def setName(self, name):        # setter for self.name
        self.name = name

    def getName(self):              # getter for self.name
        return self.name

    def setType(self, itemType):    # setter for self.type
        self.type = itemType

    def getType(self):              # getter for self.type
        return self.type

    def setPrice(self, price):      # setter for self.price
        self.price = price

    def getPrice(self):             # getter for self.price
        return self.price

    def setDescription(self, description):  # setter for self.description
        self.description = description

    def getDescription(self):           # getter for self.description
        return self.description

    # message to be printed out when printing an object
    # includes all 4 attributes
    def __str__(self):
        msg = self.name + " (" + self.type + "): $" + str(self.price) + "\n\t " + self.description
        return msg
