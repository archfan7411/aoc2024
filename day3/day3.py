# Advent of Code Day 3
# Joseph Daly 2024-12-03

s = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        for i,c in enumerate(line):
            if line[i-3:i+1] == "mul(":
                close_index = i + line[i:].find(")")
                number_pair = line[i+1:close_index]
                numbers = number_pair.split(",")
                if len(numbers) != 2:
                    continue
                try:
                    num1 = int(numbers[0])
                    num2 = int(numbers[1])
                    s += num1 * num2
                except:
                    continue

print(s)
