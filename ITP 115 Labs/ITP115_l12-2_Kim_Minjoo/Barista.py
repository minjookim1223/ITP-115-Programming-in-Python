# Minjoo Kim
# ITP 115, Fall 2019
# L12-2
# minjook@usc.edu

# Barista Object

#import coffee
from Coffee import Coffee

# create Barista object
class Barista(object):

    # for the max order (class variable)
    MAX_ORDER = 5

    # 2 instance attributes/variables
    # name of the barista and the list for the orders
    def __init__(self, nameBarista):
        self.name = nameBarista
        self.orders = []

    # take orders and make a coffee object. print the order
    def takeOrder(self):
        # Ask the customer what they want
        drink = input("What drink do you want? ")
        size = input("What size would you like? ")
        name = input("What is your name? ")
        # create the coffee object
        coffee = Coffee(size, drink, name)
        # add the object in the order
        self.orders.append(coffee)
        # print the order
        print(coffee)

    # the maximum number of orders is 5
    def isAcceptingOrders(self):
        # if the order list is less than 5, then accept the order
        if len(self.orders) < Barista.MAX_ORDER:
            return True
        # if not, complete the orders first
        else:
            print("Here are the completed orders:")
            return False

    # make the drinks
    def makeDrinks(self):
        # created a variable to keep track of how many orders you can have
        length = len(self.orders)
        # loop through the orders
        for i in range(length):
            # make sure to set the index to completed
            Coffee.setCompleted(self.orders[i])
            # print the orders that are completed
            print("\t", end="")
            print(self.orders[i])

    # for printing barista
    def __str__(self):
        greetings = "Hello, my name is " + self.name + ", and I am your barista."
        return greetings



