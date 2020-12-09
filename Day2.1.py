file1 = open('PuzzleInput2.txt', 'r') 
Lines = file1.readlines()

def check_password(password):
    parts = password.split()
    numbers = parts[0].split('-')
    character = parts[1][0]
    count_char = 0
    for x in parts[2]:
        if(x == character):
            count_char += 1
    if(count_char >= int(numbers[0]) and count_char <= int(numbers[1])):
        return True
    return False

print(Lines[0])
check_password(Lines[0])

count = 0
for line in Lines:    
    check = check_password(line)
    if(check == True):
        count += 1
        print(line)

print('Count: {}'.format(count))



