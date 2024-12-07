num = 0

def count_validities(result, numbers, interim, index=0):
    count = 0
    if interim > result:
        return 0
    if index == len(numbers)-1:
        if interim == result:
            return interim
        return 0
    count += count_validities(result, numbers, interim+numbers[index+1], index+1)
    count += count_validities(result, numbers, interim*numbers[index+1], index+1)
    concatenation = int(str(interim)+str(numbers[index+1]))
    count += count_validities(result, numbers, concatenation, index+1)
    return count

with open("input.txt", "r") as f:
    for line in f.readlines():
        items = line.split(":")
        result = int(items[0])
        numbers = [int(x) for x in items[1].strip().split(" ")]
        # I misunderstood at first and thought we were summing all valid solutions
        num += result if count_validities(result, numbers, numbers[0]) != 0 else 0

print(num)