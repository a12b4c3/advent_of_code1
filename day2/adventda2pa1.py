
problemPath = "C:\\advent_of_code\\day2\\day2problem.txt"
problemFile = open(problemPath, "r")

## global variables
listifiedProblem = list([])
doublesAndTriples = list([0,0])

def main():
    listifyProblem()
    walkTheProblem()
    printSolution()


def listifyProblem():
    for line in problemFile:
        listifiedProblem.append(line.rstrip())

def walkTheProblem():
    for item in listifiedProblem:
        alphabetCounter = list([0])*26
        for char in item:
            number = abcTo123(char)
            alphabetCounter[number] = alphabetCounter[number]+1
        if 2 in alphabetCounter:
            doublesAndTriples[0] = doublesAndTriples[0]+1
        if 3 in alphabetCounter:
            doublesAndTriples[1]= doublesAndTriples[1]+1

def printSolution():
    solution = doublesAndTriples[0] * doublesAndTriples[1]
    print("the checksum is " + str(solution))

def abcTo123(abc):
    switcher = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25
    }
    func = switcher.get(abc, lambda: "invalid alphabet")
    return func

if __name__ == "__main__":
    main()
