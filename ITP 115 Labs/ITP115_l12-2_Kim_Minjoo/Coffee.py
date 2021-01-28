# Minjoo Kim
# ITP 115, Fall 2019
# L12-2
# minjook@usc.edu

# coffee object
class Coffee(object):

    # class variable (list) to show the user whether the order will be completed or not
    STATUSES = ["(ordered)", "(completed)"]

    # instance variables
    def __init__(self, size, description, nameCustomer):
        self.size = size
        self.desc = description
        self.customer = nameCustomer
        self.statusIndex = 0

    # if the order is completed, index becomes 1
    def setCompleted(self):
        self.statusIndex = 1

    # print a nice little message for the order
    def __str__(self):
        return str(self.size) + " " + str(self.desc) + " for " + str(self.customer) + (
                " " + str(Coffee.STATUSES[self.statusIndex]))








