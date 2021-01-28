# Minjoo Kim
# ITP 115, Fall 2019
# L8-2
# minjook@usc.edu

# This program simulates a temperature calculator based on given inputs


def main():

    repeat = True

    while repeat:   # condition to repeat this program
        print("Welcome to the Temperature Converter 1.0")   # greeting

        converter = int(input("Enter 1 for F->C, or 2 for C->F: "))  # accept input for c->f or f->c
        inputTemperature = int(input("Enter input temperature: "))  # accept input temperature

        # if converter the converter has the right input, go on
        if converter == 1 or converter == 2:    # condition to call the functions
            converted = temperatureConverter(converter, inputTemperature)   # call the temperatureConverter
            print("The converter temperature is " + str(converted))     # print out the temperature

        # if converter has the wrong input, do not call the functions.
        else:
            print("Invalid conversion code")    # print that it won't accept the conversion code
            print("The converted temperature is 0")     # converted temp is 0

        repeat = wantsToContinue()      # ask if it wants to repeat
        print("")       # print a line to make it pretty


# this function calculates the conversion based on user's inputs: conversion Type and inputTemperature
def temperatureConverter(conversionType, inputTemperature):
    if conversionType == 1:     # the user chose f->c
        return (inputTemperature - 32) * 5.0 / 9       # convert f -> c

    elif conversionType == 2:   # the user chose c -> f
        return (inputTemperature * 9 / 5) + 32  # convert c-> f


# this function will return the condition that is necessary to repeat this program
# (the condition necessary to repeat the while loop)
# True for repeating and False for quitting
def wantsToContinue():
    repeat = "A"        # declare a repeat variable
    while repeat != "Y" or repeat != "N":       # if repeat has the right input
        repeat = input("Do you want to continue?: ")    # continue to ask if the user wants to go on
        if repeat == "Y" or repeat == "y":      # if user says yes (Y or y)
            return True     # return True
        elif repeat == "N" or repeat == "n":      # if user says no (N or n)
            return False        # return False


main()
