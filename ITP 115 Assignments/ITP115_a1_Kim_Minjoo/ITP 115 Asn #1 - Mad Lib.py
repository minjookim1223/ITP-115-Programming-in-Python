# Minjoo Kim
# ITP 115, Fall 2019
# Assignment #1
# minjook@usc.edu

# Description:
# This program simulates a game called "Mad Lib"


def main():

    year = int(input("Enter a number: "))  # Take an integer (#1) as an input
    classNumber = int(input("Enter a number: "))  # Take an integer (#2) as an input
    firstSubject = input("Enter a major/minor/concentration from USC: ")  # Take a string (#1) as an input
    classNumbers = int(input("Enter a number: "))  # Take an integer (#3) as an input
    secondSubject = input("Enter a different major/minor/concentration from USC: ")  # Take a string (#2) as an input
    adjective = input("Enter an adjective: ")  # Take a string (#3) as an input
    decimal = float(input("Enter a decimal greater than 0 and less than 4: "))  # Take a float as an input
    verb = input("Enter a verb ending with -ing: ")  # Take a string (#4) a an input
    place = input("Enter a place (proper noun, i.e. Disneyland): ")  # Take a string (#5) a an input
    # 3 integers, 5 strings, 1 float

    print("\n")  # Print to a new line to give some space between the story and all the input commands

    # Utilized if/elif/else functions to deal with counting conventions (1st, 2nd, 3rd, 4th, etc.)
    # Hello, I am a "NUMBER"th year at USC.
    if year == 1:
        print("Hello, I am a \"" + str(year) + "\"st year at USC.")  # "1st" year
    elif year == 2:
        print("Hello, I am a \"" + str(year) + "\"nd year at USC.")  # "2nd" year
    elif year == 3:
        print("Hello, I am a \"" + str(year) + "\"rd year at USC.")  # "3rd" year
    else:
        print("Hello, I am a \"" + str(year) + "\"th year at USC.")  # "4th" year

    # All integers and floats have been formatted as string for concatenation issues

    # I am taking NUMBER OF "CLASSES" + class(es) about "CONCENTRATION".
    print("I am taking \"" + str(classNumber) + "\" class(es) about \"" + firstSubject + "\".")

    # I am also taking "NUMBER" class(es) about "CONCENTRATION".
    print("I am also taking \"" + str(classNumbers) + "\" class(es) about \"" + secondSubject + "\".")

    # This means that I am taking "ADDITION OF INTEGERS" class(es) total!
    print("This means I am taking \"" + str(classNumber + classNumbers) + "\" class(es) total!")

    # I am very "ADJECTIVE" to take these classes.
    print("I am very \"" + adjective + "\" to take these classes.")

    # I hope my GPA is going to be at least "DECIMAL" by end of this semester.
    print("I hope my GPA is going to be at least \"" + str(decimal) + "\" by end of this semester.")

    # Apart from school, I will be "VERB -ing" every day at "PLACE".
    print("Apart from school, I will be \"" + verb + "\" every day at \"" + place + "\".")

    # Concluding sentence.
    print("Pleased to meet you all!")


main()