# Advent of Code Day 9
# Joseph Daly 2024-12-09

def checksum(filesystem):
    result = 0
    for i, value in enumerate(filesystem):
        if value != -1:
            result += i*value
    return result

def print_fs(filesystem):
    result = ""
    for value in filesystem:
        if value == -1:
            result += "."
        else:
            result += str(value)
    print(result)

with open("input.txt", "r") as f:
    filesystem = []
    block_id = 0
    for line in f.readlines():
        data = [int(x) for x in line.strip()]
        for i, value in enumerate(data):
            if i%2==0: # file block
                filesystem += [block_id]*value
                block_id += 1
            else:
                filesystem += [-1]*value
        break

    sorted = False

    while not sorted:
        dot_index = -1
        last_index = -1
        for i, value in enumerate(filesystem):
            if value==-1:
                if dot_index == -1:
                    dot_index = i
            else:
                last_index = i
        if dot_index < last_index:
            filesystem[dot_index] = filesystem[last_index]
            filesystem[last_index] = -1
        else:
            sorted = True

    print(checksum(filesystem))

