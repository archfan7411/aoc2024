# Advent of Code Day 3 Part 2
# Joseph Daly 2024-12-03

s = 0

enabled = True

with open("input.txt", "r") as f:
    for line in f.readlines():
        for i,c in enumerate(line):
            if line[i-3:i+1] == "mul(" and enabled:
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
                print(num1, num2)
            elif line[i-2:i] == "do":
                enabled = True
            elif line[i-5:i] == "don't":
                enabled = False


print(s)
