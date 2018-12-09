
## edit the filepath
filepath = "C:\\advent_of_code\\day1small.txt"

## load the file
file = open(filepath, "r")

## declare and initialize the variables
## finalFrequency is an integer, representing the frequency after each change
## frequencies is an arraylist, representing the list of frequencies
## repetition_index is an arraylist, representing the next index where the frequency is the same as the current frequency.

finalFrequency = 0
frequencies = []
repetition_index = []
for line in file:
    line.rstrip()
    finalFrequency += int(line)
    frequencies.append(finalFrequency)
    #list.append(line[:-1])
    #print(line)


#part1 = open("C:\\advent_of_code\\day1part1ans.txt", "w+")
#part1.write(str(frequencies))

large_idx = 999999
## for each element in the list of frequencies find the one that repeats the earliest
for idx,ele in enumerate(frequencies):
    idxHolder = 0
    for idx2,ele2 in enumerate(frequencies[idx+1:]):
        ## if ele2 matches ele
        # print(str(ele) + " vs " + str(ele2))
        if ele2 == ele:
            idxHolder = idx + idx2 + 1
            break
            # print(" /element2: " + str(ele2) + " /at index: " + str(idx2+idx+1) + " /element1: " + str(ele) + " /at index: " + str(idx))

    if idxHolder != 0:
        repetition_index.append(idxHolder)
    else:
        repetition_index.append(large_idx)

## print the solution
print("//frequencies")
print(frequencies)
print("-------------")
print("//repetition index")
print(repetition_index)
print("------------------")
print("size of frequencies: " + str(len(frequencies)) + " size of repetition index: " +str(len(repetition_index)))

## check that both array lists are of the same size...
assert(len(frequencies) == len(repetition_index))

## find the index of the lowest item in the list
curr_smallest_index = 99999
for idx,ele in enumerate(repetition_index):
    if ele < curr_smallest_index:
        curr_smallest_index = ele

print("current smallest index: "  + str(curr_smallest_index))

print("========== final solution ==========")
if curr_smallest_index != 99999:
    print(str(curr_smallest_index) + " is the smallest index of the first repeat" )
    print(str(frequencies[curr_smallest_index]) + " is the value of the first repeat")
else:
    print("no repeating elements")
