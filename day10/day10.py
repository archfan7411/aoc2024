# Advent of Code Day 10
# Joseph Daly 2024-12-10

class Map:
    """A representation of a topographical map. Charred areas are represented with -1 depth."""
    def __init__(self, lines):
        self.lines = lines
    
    def get(self, x, y):
        """Returns the value at a given position"""
        if x < 0 or x > len(self.lines[0])-1 or y < 0 or y > len(self.lines) - 1:
            return -1
        return self.lines[y][x]
    
    def trailheads(self):
        """Returns all trailhead positions in the map"""
        trailheads = []
        for y, line in enumerate(lines):
            for x, value in enumerate(line):
                if value == 0:
                    trailheads.append((x,y))
        return trailheads
    
    def print(self):
        """Prints a representation of the map"""
        print("\n".join(["".join([(str(x) if x>=0 else ".") for x in l]) for l in self.lines]))
    

def follow_trail(map, x, y):
    """Returns number of accessible 9s from a given location"""
    value = map.get(x,y)
    if value == 9:
        return [(x, y)]
    locations = [] # all trail terminators found

    targets = [ # Everywhere we cna go from this spot
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1)
    ]
    for x2, y2 in targets:
        if map.get(x2, y2) == value+1: # valid next step
            locations += follow_trail(map, x2, y2)
    
    # Sometimes different paths reach the same terminator
    # We only care about how many unique terminators we can reach
    removed_duplicates = []
    for location in locations:
        if not (location in removed_duplicates):
            removed_duplicates.append(location)
    
    return removed_duplicates


with open("input.txt", "r") as f:
    lines = []
    for line in f.readlines():
        # Read all values, representing charred areas with -1 depth
        lines.append([(int(x) if x!="." else -1) for x in line.strip()])
    
    mymap = Map(lines)
    trailheads = mymap.trailheads()

    total = 0
    for x, y in trailheads:
        total += len(follow_trail(mymap, x, y))
    
    print(total)
