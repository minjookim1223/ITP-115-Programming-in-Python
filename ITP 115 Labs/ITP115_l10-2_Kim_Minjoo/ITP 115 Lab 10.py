# Minjoo Kim
# ITP 115, Fall 2019
# L9-1
# minjook@usc.edu


def readFile(fileName):
    dictionaryList = []
    fileIn = open(fileName, "r")
    for line in fileIn:
        line = line.strip()
        dictionaryList.append(line)

    fileIn.close()
    return dictionaryList


def findWord(wordList, searchWord):
    for i in range(len(wordList)):
        if searchWord == wordList[i]:
            return True
            break
        else:
            return False


def writeFile(outputList, fileName):
    fileOut = open(fileName, "w")
    for i in range(len(outputList)):
        print(outputList[i], file=fileOut)


def main():
    print("Welcome to Word Checker")

    fileNameRead = input("Enter the name of the file you wish to read in: ")
    dictionaryList = readFile(fileNameRead)

    fileNameWrite = input("Enter the name of the file you wish to write to: ")
    searchWord = input("Enter the word you wish to check: ")
    word = findWord(dictionaryList, searchWord)

    if word:
        writeFile(dictionaryList, fileNameWrite)
    if not word:
        dictionaryList.append(searchWord)
        dictionaryList.sort()
        writeFile(dictionaryList, fileNameWrite)
        print("The word " + searchWord + " has been written to " + fileNameWrite)


main()
