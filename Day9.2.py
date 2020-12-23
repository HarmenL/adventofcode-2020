file1 = open('PuzzleInput9.txt', 'r')
input = file1.readlines()

i = 0
numbers = []
for line in input:
    numbers.append(int(line.strip()))


find = 20874512

valid = []

total = 0
using = []
i = 0
for number in numbers:
    j = i + 1
    total = number
    using = []
    using.append(number)
    while total < find:
        number_to_add = numbers[j]
        total += number_to_add
        using.append(number_to_add)
        if(total == find):
            print("FOUND: {}".format(using))
            break
        j += 1
    i += 1
    if(total == find):
        break

print("Using:{}".format(using))
print("Total:{}".format(total))
max_value = max(using)
min_value = min(using)
print("Max:{}".format(max_value))
print("Min:{}".format(min_value))
answer = max_value + min_value

print("Answer:{}".format(answer))


# 3012420 correct