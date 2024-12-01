# Advent of Code Day 1
# Joseph Daly 2024-12-01

list1 = []
list2 = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        s = line.split()
        list1.append(int(s[0]))
        list2.append(int(s[1]))

list1.sort()
list2.sort()

score = 0

for l in list1:
    count = list2.count(l)
    score += count*l

print(score)