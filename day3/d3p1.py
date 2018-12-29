import re

filepath = "day3problem.txt"
problem_list = list()

def main(filepath):
    file_handler(filepath)
    conflict_list = problem_solver()
    print(conflict_list)
    print(sum(conflict_list))
    find_negative(conflict_list)


def file_handler(filepath):
    with open(filepath,"r") as problem_file:
        for entry in problem_file:
            entry = entry.rstrip()
            entry_list = reg_ex_parsing(entry)
            problem_list.append(entry_list)


def reg_ex_parsing(line):
    regex = "#(\d*)\s@\s(\d*),(\d*):\s(\d*)x(\d*)"
    entry = re.match(regex, line).groups()
    return entry


def problem_solver():
    conflict_list = list()
    for item_number, request in enumerate(problem_list):
        conflict = check_for_conflicts(request, item_number)
        conflict_list.append(False)
        if conflict:
            conflict_list[-1] = True
            continue
    return conflict_list


def check_for_conflicts(request, item_number):
    for idx, other_request in enumerate(problem_list):
        if idx == item_number:
            continue
        else:
            r1_x1 = int(request[1])
            r1_y1 = int(request[2])
            r1_x2 = int(request[1]) + int(request[3])
            r1_y2 = int(request[2]) + int(request[4])

            r2_x1 = int(other_request[1])
            r2_y1 = int(other_request[2])
            r2_x2 = int(other_request[1]) + int(other_request[3])
            r2_y2 = int(other_request[2]) + int(other_request[4])

            r2_left_of_r1 = r2_x1 >= r1_x2
            r1_left_of_r2 = r1_x1 >= r2_x2
            r2_top_of_r1 = r2_y2 <= r1_y1
            r1_top_of_r2 = r1_y2 <= r2_y1

            conflict_bool = not (r2_left_of_r1 or r1_left_of_r2 or r2_top_of_r1 or r1_top_of_r2)

            if conflict_bool:
                return True


def find_negative(conflicts):
    counter = 0
    for value in conflicts:
        print(value)
        counter += 1
        if value is False:
            print(counter)
            print("found")
            exit()



if __name__ == "__main__":
    main(filepath)