# Advent of Code Day 6
# Joseph Daly 2024-12-06

lines = []

steps = {
    "up": (0,-1),
    "down": (0,1),
    "left": (-1,0),
    "right": (1,0)
}

def walk_map(lines):
    direction = "up"
    starting = True
    positions = []
    moves = []
    start_pos = (0,0)
    while True:
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == "^":
                    if starting:
                        start_pos = (x, y)
                    starting = False
                    if (x, y, direction) in moves:
                        return "loop"
                    moves.append((x, y, direction))
                    dX, dY = steps[direction]
                    if y+dY < 0 or y+dY > len(lines)-1 or x+dX < 0 or x+dX > len(line)-1:
                        lines[y] = line[:x] + "X" + line[x+1:]
                        if (x, y) != start_pos and not ((x, y) in positions):
                            positions.append((x,y))
                        return positions
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
                        if (x, y) != start_pos and not ((x, y) in positions):
                            positions.append((x,y))
                    break

num = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        lines.append(line.strip("\n"))
    positions = walk_map(lines.copy())
    for x, y in positions:
        print("Testing ", x, ",", y)
        victim = lines.copy()
        victim[y] = victim[y][:x] + "#" + victim[y][x+1:]
        if walk_map(victim) == "loop":
            print("Loop found!")
            num += 1
    print(num)

