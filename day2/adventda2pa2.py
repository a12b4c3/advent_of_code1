
problemPath = "C:\\advent_of_code\\day2\\day2problem.txt"
problemFile = open(problemPath, "r")

## global variables
listifiedProblem = list([])
currentFirst = ""
currentSecond = ""

def main():
    listifyProblem()
    walkTheProblem()
    printSolution()


def listifyProblem():
    for line in problemFile:
        listifiedProblem.append(line.rstrip())

def walkTheProblem():
    for index,item in enumerate(listifiedProblem):
        currentFirst = item
        for item in listifiedProblem[index+1:]:
            currentSecond = item
            checkForMatches(currentFirst, currentSecond)

def checkForMatches(first, second):
    mismatches = 0
    strIndex = 0
    while True:
        if first[strIndex] != second[strIndex]:
            mismatches += 1
        if mismatches > 1:
            return
        strIndex += 1
        if strIndex == len(first)-1 and mismatches < 2:
            print("match found")
            print(first)
            print(second)
            exit()


def printSolution():
    pass


if __name__ == "__main__":
    main()
