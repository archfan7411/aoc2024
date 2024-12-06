# Advent of Code Day 6
# Joseph Daly 2024-12-06

lines = []

steps = {
    "up": (0,-1),
    "down": (0,1),
    "left": (-1,0),
    "right": (1,0)
}

def count_Xs(lines):
    num = 0
    for line in lines:
        num += line.count("X")
    return num

def walk_map(lines):
    direction = "up"
    while True:
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "^":
                    dX, dY = steps[direction]
                    if y+dY < 0 or y+dY > len(lines)-1 or x+dX < 0 or x+dX > len(line)-1:
                        lines[y] = line[:x] + "X" + line[x+1:]
                        return count_Xs(lines)
                    target = lines[y+dY][x+dX]
                    if target == "#":
                        if direction == "up":
                            direction = "right"
                        elif direction == "down":
                            direction = "left"
                        elif direction == "left":
                            direction = "up"
                        elif direction == "right":
                            direction = "down"
                    else:
                        lines[y+dY] = lines[y+dY][:x+dX] + "^" + lines[y+dY][x+dX+1:]
                        lines[y] = lines[y][:x] + "X" + lines[y][x+1:]
                    break

with open("input.txt", "r") as f:
    for line in f.readlines():
        lines.append(line.strip("\n"))
    print(walk_map(lines))
