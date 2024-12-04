# Advent of Code Day 4
# Joseph Daly 2024-12-04

num = 0

with open("input.txt", "r") as f:
    lines = list(f.readlines())
    for li, line in enumerate(lines):
        for ci, char in enumerate(line):
            if char == "X":
                # Left
                if ci >= 3:
                    if line[ci-3:ci] == "SAM":
                        num += 1
                # Right
                if line[ci:ci+4] == "XMAS":
                    num += 1
                # Up
                if li >= 3:
                    if lines[li-1][ci] == "M" and lines[li-2][ci] == "A" and lines[li-3][ci] == "S":
                        num += 1
                # Down
                if li+3 < len(lines):
                    if lines[li+1][ci] == "M" and lines[li+2][ci] == "A" and lines[li+3][ci] == "S":
                        num += 1
                
                # Down left
                if li >= 3 and ci >= 3:
                    if lines[li-1][ci-1] == "M" and lines[li-2][ci-2] == "A" and lines[li-3][ci-3] == "S":
                        num += 1
                
                # Up right
                if li >= 3 and ci+3 < len(line):
                    if lines[li-1][ci+1] == "M" and lines[li-2][ci+2] == "A" and lines[li-3][ci+3] == "S":
                        num += 1

                # Down left
                if li+3 < len(lines) and ci >= 3:
                    if lines[li+1][ci-1] == "M" and lines[li+2][ci-2] == "A" and lines[li+3][ci-3] == "S":
                        num += 1
                
                # Down right
                if li+3 < len(lines) and ci+3 < len(line):
                    if lines[li+1][ci+1] == "M" and lines[li+2][ci+2] == "A" and lines[li+3][ci+3] == "S":
                        num += 1

print(num)