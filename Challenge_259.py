import math
layout = {
    "1": [0, 0], "2": [1, 0], "3": [2, 0],
    "4": [0, 1], "5": [1, 1], "6": [2, 1],
    "7": [0, 2], "8": [1, 2], "9": [2, 2],
    ".": [0, 3], "0": [1, 3], " ": [2, 3] }

input = raw_input("Enter an ip address: ")
curPos = layout[input[0]]
distance = 0

for i in range(1, len(input)):
    dx = curPos[0] - layout[input[i]][0]
    dy = curPos[1] - layout[input[i]][1]
    curPos = layout[input[i]]
    distance += math.sqrt(dx**2 + dy**2)

print "Distance: {:.2f} cm".format(distance)