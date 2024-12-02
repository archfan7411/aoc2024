# Advent of Code Day 2
# Joseph Daly 2024-12-02

safe = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        l = [int(i) for i in line.split()]
        smooth = True
        decreasing = True
        increasing = True
        for i, x in enumerate(l):
            if i==0:
                continue
            prev = l[i-1]
            if x > prev:
                decreasing = False
            if x < prev:
                increasing = False
            delta = abs(x-l[i-1])
            if delta < 1 or delta > 3:
                smooth = False
        
        if smooth and (decreasing or increasing):
            safe += 1

print(safe)