# Advent of Code Day 5 Part 2
# Joseph Daly 2024-12-05

order = []

done_reading_rules = False

medians = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        if len(line.strip()) == 0:
            done_reading_rules = True
        else:
            if not done_reading_rules:
                split = [int(x.strip()) for x in line.split("|")]
                before = split[0]
                after = split[1]
                order.append((before, after))
            else: # read instructions
                instructions = [int(x.strip()) for x in line.split(",")]
                valid = True
                for rule in order:
                    before, after = rule
                    if (before in instructions and after in instructions) and (instructions.index(after) < instructions.index(before)):
                        valid = False
                        break
                if not valid:
                    while not valid:
                        valid = True
                        for rule in order:
                            before, after = rule
                            if (before in instructions and after in instructions) and (instructions.index(after) < instructions.index(before)):
                                valid = False
                                b_index = instructions.index(before)
                                a_index = instructions.index(after)
                                instructions[b_index] = after
                                instructions[a_index] = before
                    median = instructions[len(instructions)//2]
                    medians += median

print(medians)