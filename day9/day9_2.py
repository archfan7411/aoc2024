# Advent of Code Day 9 Part 2
# Joseph Daly 2024-12-09

def checksum(filesystem):
    memory = []
    result = 0
    for id, size in filesystem:
        memory += [id]*size
    
    for i, value in enumerate(memory):
        if value != -1:
            result += i*value

    return result

def print_fs(filesystem):
    result = ""
    for id, size in filesystem:
        if id == -1:
            result += "."*size
        else:
            result += str(id)*size
    print(result)

with open("input.txt", "r") as f:
    filesystem = []
    block_id = 0
    for line in f.readlines():
        data = [int(x) for x in line.strip()]
        for i, value in enumerate(data):
            if i%2==0: # file block
                filesystem.append([block_id, value])
                block_id += 1
            else:
                filesystem.append([-1, value])
        break

    for block_id in range(block_id, -1, -1):
        block_index = -1
        for i, block in enumerate(filesystem):
            if block[0] == block_id:
                block_index = i
        
        usable_index = -1
        for i, block in enumerate(filesystem):
            # Blank and big enough
            if block[0] == -1 and block[1] >= filesystem[block_index][1]:
                usable_index = i
                break
        
        # we found one and it's to the left
        if usable_index != -1 and usable_index < block_index:
            # remove blank space
            block_size = filesystem[block_index][1]
            filesystem[usable_index][1] -= filesystem[block_index][1]
            moving_block = filesystem.pop(block_index)
            filesystem.insert(usable_index, moving_block)
            filesystem.insert(block_index+1, [-1, block_size])

    print(checksum(filesystem))
