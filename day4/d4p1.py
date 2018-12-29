import re
import datetime

# main
def main():
    filepath = input("what is the problem name? \n >> ")
    sorted_problem = []
    if filepath == "":
        filepath = "d4input.txt"
    input_handler(filepath, sorted_problem)
    input_sorter(sorted_problem)
    input_saver(sorted_problem)


# input handler
# opens the file and processes it by removing trailing spaces and extraneous data
def input_handler(filepath, sorted_problem):
    with open(filepath, "r") as problem_file:
        for line in problem_file:
            line = line.rstrip()
            arrayify(line, sorted_problem)
    print(sorted_problem)


# makes a 2d array
# takes each line of input and makes it into an array
def arrayify(line, sorted_problem):
    # regex_pattern = "\[1518-(\d{2})-(\d{2})\s(\d{2}):(\d{2})]\s(.*)"
    regex_pattern = "\[(.*)\]\s(.*)"
    entry = re.match(regex_pattern, line).groups()
    sorted_problem.append(entry)


# input sorter
# sorts the input into chronological order
def input_sorter(sorted_problem):
    sorted_problem.sort(key=lambda sub: (datetime.datetime.strptime(sub[0],"%Y-%m-%d %H:%M")))
    print(sorted_problem)

# input saver
# saves the chronologically sorted data
def input_saver(sorted_problem):
    output = open("sorted_input.txt", "w")
    for entry in sorted_problem:
        output.write(str(entry)[1:-1])
        output.write("\n")
    output.close()


if __name__ == "__main__":
    main()