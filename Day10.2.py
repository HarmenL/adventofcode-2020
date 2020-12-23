file1 = open('PuzzleInput10.txt', 'r')
input = file1.readlines()

numbers = [0]
for line in input:
    numbers.append(int(line.strip()))

numbers.append(max(numbers) + 3)

numbers.sort()
multiplier = []

for number in numbers:
    currentmultiplier = 0
    for number2 in numbers:
        if(number is number2 or number2 < number):
            continue
        if(number2 - number == 1):
            currentmultiplier += 1
        elif(number2 - number == 2):
            currentmultiplier += 1        
        elif(number2 - number == 3):
            currentmultiplier += 1
        else:
            break
    multiplier.append(currentmultiplier)


print("multiplier: {}".format(multiplier))

total = 1
for value in multiplier:
    if(value != 0 and value !=1):
        total = total * value


print("Answer: {}".format(total))
