file1 = open('PuzzleInput10.txt', 'r')
input = file1.readlines()

numbers = [0]
for line in input:
    numbers.append(int(line.strip()))

numbers.append(max(numbers) + 3)

numbers.sort()
i = 0
ones = 0
threes = 0
for number in numbers:
    if(i + 1 == len(numbers)):
        break
    difference = numbers[i + 1] - number
    print(difference)
    if(difference == 1):
        ones += 1
    if(difference == 3):
        threes +=1 
    

    i += 1

print("One:{} / Three:{}".format(ones, threes))
print("Answer: {}".format(ones * threes))