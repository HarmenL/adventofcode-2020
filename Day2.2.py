file1 = open('PuzzleInput2.txt', 'r') 
Lines = file1.readlines()

def check_password(password):
    parts = password.split()
    numbers = parts[0].split('-')
    character = parts[1][0]
    first = False
    second = False
    if(parts[2][int(numbers[0]) - 1] == character) :
        first = True
    if(parts[2][int(numbers[1]) - 1] == character) :
        second = True
    if(first == True and second == False) :
        return True
    if(first == False and second == True) :
        return True    
    return False

result1 = check_password("1-3 b: cdefg")
print(result1)


count = 0
for line in Lines:    
    check = check_password(line)
    if(check == True):
        count += 1
        print(line)

print('Count: {}'.format(count))



