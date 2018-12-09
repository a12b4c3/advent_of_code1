import re

# fill in filepath here
filepath = "day3problem.txt"

# problemArray is a list that should have the following...
    # id number
    # top left corner coordinate
    # rectangle dims
problemArray = list([])
overlapped_requests = list()

# overlapArray is a boolean array that tracks whether an ID is already overlapping with some other cloth...
# boolean array of length n, where n is the number of IDs


def main(path):
    filepath = path
    file_handler(filepath)


#   problemArray[?] where ? is 0 to n, is the id of the request
#   problemArray[?][x] where x is 0 to 4, is the parameter
#   x = 0, represents the id of the request
#   x = 1, represents the x axis of the top left corner
#   x = 2, represents the y axis of the top left corner
#   x = 3, represents the width of the cloth
#   x = 4, represents the height of the cloth
#   eg. problemArray[2][4] returns the height of the 3rd cloth request.

def file_handler(filepath):
    with open(filepath, "r") as problemFile:
        for line in problemFile:
            line = line.rstrip()
            clothRequest = reg_ex_parsing(line)
            problemArray.append(clothRequest)
    overlapped_requests = [None]*len(problemArray)


def reg_ex_parsing(line):
    regex = "#(\d*)\s@\s(\d*),(\d*):\s(\d*)x(\d*)"
    entry = re.search(regex, line).groups()
    return entry


def problem_solver():
    r1r2_overlap = false
    for cloth_request in problemArray:
        x1_1 = cloth_request[1]
        y1_1 = cloth_request[2]
        x2_1 = cloth_request[1] + cloth_request[3]
        y2_1 = cloth_request[2] + cloth_request[4]
        for idx, other_cloths in enumerate(problemArray):
            if idx == cloth_request[0]:
                continue
            else:
                x1_2 = problemArray[idx][1]
                y1_2 = problemArray[idx][2]
                x2_2 = problemArray[idx][1] + problemArray[idx][3]
                y2_2 = problemArray[idx][1] + problemArray[idx][4]
                r1r2_overlap = overlap_checker(x1_1, y1_1,x2_1, y2_1, x1_2, y1_2, x2_2, y2_2)
                if r1r2_overlap:
                    overlapped_requests[cloth_request[0]] = True
                    overlapped_requests[other_cloths[0]] = True
    overlapping_cloth_counter()


#   int int int int int int int int -> Boolean
#   returns true if squares overlap, false otherwise.

def overlap_checker(x1_1, y1_1, x2_1, y2_1, x1_2, y1_2, x2_2, y2_2):
    # r1 totally on top of r2
    bool1 = y2_1 <= y1_2
    # r1 totally on bottom of r2
    bool2 = y2_2 <= y1_1
    # r1 totally on left of r2
    bool3 = x2_1 <= x1_2
    # r1 totally on right of r2
    bool4 = x2_2 <= x1_1
    return not (bool1 or bool2 or bool3 or bool4)


def overlapping_cloth_counter():
    print(sum(overlapped_requests))


if __name__ == "__main__":
    main(filepath)