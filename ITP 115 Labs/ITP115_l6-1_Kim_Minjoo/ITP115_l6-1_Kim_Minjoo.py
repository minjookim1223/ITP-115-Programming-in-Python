# Minjoo Kim
# ITP 115, Fall 2019
# L6-1
# minjook@usc.edu


# convert the input into all uppercase or lowercase
# strip all white spaces
# convert those words to two separate list
# check if the words are anagrams of each other (same length and same letters)
# Use a for loop to check if each word is a palindrome (are they the same word forward and backward)
def main():
    # prompt the user to enter the words
    first = input("Please enter a word or statement: ")
    second = input("Please enter a second word of statement: ")

    # turn the words into lower case
    first = first.lower()
    second = second.lower()

    # string without white spaces
    firstReplaced = first.replace(" ", "")
    secondReplaced = second.replace(" ", "")

    # turning the string into a list
    firstList = list(firstReplaced)
    secondList = list(secondReplaced)

    # sort the list
    firstList.sort()
    secondList.sort()

    # checking if the words/statements are anagrams
    anagram = True
    if len(firstList) == len(secondList):      # check if they have the same length
        for i in range(0, len(firstList), 1):
            if firstList[i] != secondList[i]:   # check if each letter matches one another in two lists
                anagram = False     # if they don't match, get out of the loop without turning the anagram into true
                break

    if anagram:
        print("The two words you entered are anagrams.")
    else:
        print("The two words you entered are not anagrams.")

    # Checking if the inputs are palindromes
    firstPalindrome = True
    for i in range(len(firstReplaced)):
        if firstReplaced[i] != firstReplaced[len(firstReplaced)- i - 1]:
            firstPalindrome = False
            break

    if firstPalindrome:
        print("The first word is a palindrome")
    else:
        print("The first word is not a palindrome")
    
    secondPalindrome = True
    for i in range(len(secondReplaced)):
        if secondReplaced[i] != secondReplaced[len(secondReplaced) - i - 1]:
            secondPalindrome = False
            break

    if secondPalindrome:
        print("The second word is a palindrome")
    else:
        print("The second word is not a palindrome")

main()

