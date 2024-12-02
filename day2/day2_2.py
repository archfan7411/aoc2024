# Advent of Code Day 2
# Joseph Daly 2024-12-02

safe = 0

def is_safe(l):
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
        
        return smooth and (decreasing or increasing)

with open("input.txt", "r") as f:
    for line in f.readlines():
        l = [int(i) for i in line.split()]
        for i in range(len(l)):
             if is_safe(l[0:i] + l[i+1:]):
                  safe += 1
                  break

print(safe)