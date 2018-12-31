import re

guard_sleep_minutes = {}

# outputs the laziest guard and how many minutes they are asleep, and
# what minute they were asleep the most.
def main():
    laziest_guard = calculate_guard_sleep_minutes()


# reads file line by line
def calculate_guard_sleep_minutes():
    with open("sorted_input.txt", "r") as problem_file:
        for line in problem_file:
            current_guard = 0
            current_start_sleep = 0
            line = line.rstrip()
            if line.find("Guard") is not -1:
                regex_pattern = "#(\d*)"
                guard_id = re.search(regex_pattern, line).group()
                # print(guard_id)
                continue
            if line.find("falls asleep") is not -1:
                regex_pattern2 = "(\d\d:\d\d)"
                current_start_sleep = re.search(regex_pattern2, line).group()
                # print(current_start_sleep)
                current_start_sleep = current_start_sleep.split(":")[1]
                # print(current_start_sleep)
                continue
            if line.find("wakes up") is not -1:
                regex_pattern3 = "(\d\d:\d\d)"
                wake_up_time = re.search(regex_pattern3, line).group()
                wake_up_time = wake_up_time.split(":")[1]
                # print(wake_up_time)
                # print(current_start_sleep)
                time_asleep = int(wake_up_time) - int(current_start_sleep)
                # print(time_asleep)
                continue



def find_most_frequently_asleep_minute():
    pass


if __name__ == "__main__":
    main()