file1 = open('PuzzleInput9.txt', 'r')
input = file1.readlines()

i = 0
numbers = []
for line in input:
    numbers.append(line.strip())


valid = []
for number in numbers:
    number = number.strip()
    
    if(i < 25):
        valid.append(number)   
        i += 1
        continue
    #print(number)
    pre_numbers = numbers[i-25:i]
    #print(pre_numbers)
    for pre_number in pre_numbers:
        for pre_number_2 in pre_numbers:
            if(pre_number is not pre_number_2):
                #print("{} + {} = {}".format(pre_number, pre_number_2, (int(pre_number) + int(pre_number_2))))

                if((int(pre_number) + int(pre_number_2)) == int(number)):
                    valid.append(number)
    i += 1

#print("valid:{}".format(valid))
invalid = []
for number in numbers:
    if(number not in valid):
        invalid.append(number)

print("Invalid:{}".format(invalid))


# 15 not correct # 20874512