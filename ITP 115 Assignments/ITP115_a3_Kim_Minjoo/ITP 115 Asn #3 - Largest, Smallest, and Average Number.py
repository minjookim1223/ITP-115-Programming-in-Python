# Minjoo Kim
# ITP 115, Fall 2019
# Assignment #3
# 9/22/2019
# minjook@usc.edu

# Description:
# This program calculates the largest, smallest, and average of given number.


def main():
    repeat = "y"

    while repeat == "y":
        number = 0
        large = -9999
        small = 9999
        total = 0
        count = 0

        print("Input an integer greater than or equal to 0 or -1 to quit:")
        while number != -1:
            number = int(input())

            if number != -1:
                if number > large:
                    large = number

                if number < small:
                    small = number

            total += number
            count += 1

        average = (total + 1) / (count - 1)

        print("The largest number is " + str(large))
        print("The smallest number is " + str(small))
        print("The average number is " + str(average))
        print("\n")
        repeat = input("Would you like to enter another set of numbers? (y/n): ")

    print("Goodbye!")


main()
