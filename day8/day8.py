# Advent of Code Day 8
# Joseph Daly 2024-12-08

nodes = {}

antinodes = []

with open("input.txt", "r") as f:
    # Find all nodes
    height = len(f.readlines())
    f.seek(0)
    width = 0
    for y, line in enumerate(f.readlines()):
        width = len(line.strip())
        for x, char in enumerate(line.strip()):
            if char != ".":
                if not (char in nodes.keys()):
                    nodes[char] = []
                nodes[char].append((x,y))
    
    for freq in nodes.keys():
        print(nodes[freq])
        for pos1 in nodes[freq]:
            for pos2 in nodes[freq]:
                if pos1==pos2:
                    continue
                
                dX = pos1[0]-pos2[0]
                dY = pos1[1]-pos2[1]

                anti1 = (pos1[0]+dX, pos1[1]+dY)
                anti2 = (pos2[0]-dX, pos2[1]-dY)

                if anti1[0] >= 0 and anti1[0] < width and anti1[1] >= 0 and anti1[1] < height and anti1 not in antinodes:
                    antinodes.append(anti1)
                if anti2[0] >= 0 and anti2[0] < width and anti2[1] >= 0 and anti2[1] < height and anti2 not in antinodes:
                    antinodes.append(anti2)
    
    print(len(antinodes))