# Advent of Code Day 11 Part 2
# Joseph Daly 2024-12-11

import math

def count_stones(stone, blinks):
    """Determine how many stones a given stone evaluates to after a number of blinks"""

    if blinks==0:
        return 1

    if stone == 0:
        return count_stones(1, blinks-1)
    
    num_digits = math.floor(math.log10(stone)+1)
    if num_digits>0 and num_digits%2==0:
        lower_half = stone % (10**(num_digits//2))
        upper_half = (stone - lower_half)//(10**(num_digits//2))

        num = 0
        num += count_stones(lower_half, blinks-1)
        num += count_stones(upper_half, blinks-1)

        return num

    return count_stones(stone*2024, blinks-1)



with open("i.txt", "r") as f:
    for line in f.readlines():
        stones = [int(x) for x in line.strip().split(" ")]

        num_stones = 0

        for stone in stones:
            num_stones += count_stones(stone, 25)
        
        print(num_stones)