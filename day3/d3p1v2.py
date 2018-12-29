import re
import math


filepath = "C:\\advent_of_code\\day3\\day3problem.txt"
problem_dict = dict()


def main(filepath):
    file_handler(filepath)
    print(problem_dict)
    print(len(problem_dict))
    find_overlapping_squares()


def file_handler(filepath):
    with open(filepath, "r") as problem_file:
        for entry in problem_file:
            entry = entry.rstrip()
            entry_list = reg_ex_parsing(entry)
            fill_in_dict(entry_list)


def reg_ex_parsing(line):
    regex = "#(\d*)\s@\s(\d*),(\d*):\s(\d*)x(\d*)"
    entry = re.match(regex, line).groups()
    return entry


def fill_in_dict(entry_list):
    xcoord_init = int(entry_list[1])
    ycoord_init = int(entry_list[2])
    xcoord_points = int(entry_list[3])
    ycoord_points = int(entry_list[4])
    expected_dict_size = xcoord_points * ycoord_points
    for x in range(expected_dict_size):
        column_indx = x % xcoord_points
        row_indx = math.floor(x / xcoord_points)
        dict_key = str(column_indx + xcoord_init) + "x" + str(row_indx + ycoord_init)
        if problem_dict.get(dict_key) is None:
            problem_dict[dict_key] = 1
        else:
            problem_dict[dict_key] += 1


def find_overlapping_squares():
    counter = 0
    for key, value in problem_dict.items():
        if value>1:
            counter += 1
    print(counter)



if __name__ == "__main__":
    main(filepath)