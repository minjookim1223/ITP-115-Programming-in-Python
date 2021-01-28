# Minjoo Kim
# ITP 115, Fall 2019
# Lab 2
# minjook@usc.edu

def main():

    coffee = input("What size coffee do you want (S, M, L)? ")
    temp = int(input("What temperature would you like (in degrees)? "))
    blend = input("What type of beans / blend would you like? ")
    cream = input("Would you like room for cream (y/n)? ")

    if coffee == 's' or 'S':
        coffee = "small"
    elif coffee == 'm' or 'M':
        coffee = "medium"
    elif coffee == 'l' or 'L':
        coffee = "large"
    else:
        coffee == "unknown"

    if temp > 100:
        temperature = "boiling"
    elif temp > 36 or temp < 100:
        temperature = "hot"
    elif temp > 0 or temp < 36:
        temperature = "cold"
    else:
        temperature = "frozen"

    if cream == 'y':
        print("You ordered a " + coffee + " " + temperature + " " + blend + " with cream")
    elif cream == 'n':
        print("You ordered a " + coffee + " " + temperature + " " + blend + " without cream")
    else:
        print("You ordered a " + coffee + " " + temperature + " " + blend)
        print("No known cream")


main()
