# Advent of Code Day 4
# Joseph Daly 2024-12-04

num = 0

with open("input.txt", "r") as f:
    lines = list(f.readlines())
    for li, line in enumerate(lines):
        for ci, char in enumerate(line):
            if char == "A" and ci > 0 and li > 0 and ci < len(line)-1 and li < len(lines)-1:
                if (lines[li-1][ci-1] == "M" and lines[li+1][ci+1] == "S") or (lines[li-1][ci-1] == "S" and lines[li+1][ci+1] == "M"):
                    if (lines[li-1][ci+1] == "M" and lines[li+1][ci-1] == "S") or (lines[li-1][ci+1] == "S" and lines[li+1][ci-1] == "M"):
                        num += 1

print(num)