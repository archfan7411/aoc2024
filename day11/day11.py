# Advent of Code Day 11
# Joseph Daly 2024-12-11

def blink(line):
    # Zeroes become 1s
    # Split stones with even numbers of digits
    # Else multiply by 2024
    new_line = []
    for stone in line:
        str_repr = str(stone)
        if stone == 0:
            new_line.append(1)
        elif len(str_repr)%2 == 0:
            new_line.append(int(str_repr[:len(str_repr)//2]))
            new_line.append(int(str_repr[len(str_repr)//2:]))
        else:
            new_line.append(stone*2024)
    
    return new_line


with open("input.txt", "r") as f:
    for line in f.readlines():
        stones = [int(x) for x in line.strip().split(" ")]

        for i in range(25):
            stones = blink(stones)

        print(len(stones))
        break