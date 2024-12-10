# Advent of Code Day 10 Part 2
# Joseph Daly 2024-12-10

startmap = []

class Map:
    def __init__(self, lines):
        self.lines = lines
    
    def get(self, x, y):
        if x < 0 or x > len(self.lines[0])-1 or y < 0 or y > len(self.lines) - 1:
            return -1
        return self.lines[y][x]
    
    def trailheads(self):
        trailheads = []
        for y, line in enumerate(lines):
            for x, value in enumerate(line):
                if value == 0:
                    trailheads.append((x,y))
        return trailheads
    
    def print(self):
        print("\n".join(["".join([(str(x) if x>=0 else ".") for x in l]) for l in self.lines]))
    

def follow_trail(map, x, y):
    """Returns number of trails to 9s from a given location"""
    value = map.get(x,y)
    if value == 9:
        return 1
    trails = 0 # num unique paths found
    targets = [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1)
    ]
    for x2, y2 in targets:
        if map.get(x2, y2) == value+1: # valid next step
            trails += follow_trail(map, x2, y2)
    
    return trails


with open("input.txt", "r") as f:
    lines = []
    for line in f.readlines():
        lines.append([(int(x) if x!="." else -1) for x in line.strip()])
    
    mymap = Map(lines)
    
    trailheads = mymap.trailheads()

    total = 0

    for x, y in trailheads:
        total += follow_trail(mymap, x, y)
    
    print(total)
