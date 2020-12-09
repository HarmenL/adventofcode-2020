file1 = open('PuzzleInput3.txt', 'r') 
Lines = file1.readlines()

y = len(Lines)
x = len(Lines[0])

print(x)
print(y)

def split(word):
    word = word.rstrip("\n")
    return [char for char in word]

matrix = [[0 for i in range(x)] for i in range(y)] 

index = 0
for read_line in Lines:
    split_line = split(read_line)
    matrix[index] = split_line
    index += 1

# for line in matrix:
#     print(line)

index_x = 0
index_y = 0

count = 0
while (index_y < 323) :
    value_found = matrix[index_y][index_x]
    if(value_found == '#'):
        count += 1
    index_y += 1
    index_x += 3
    print("X:{} Y:{}".format(index_x, index_y))
    if(index_x >= 31):
        index_x -= 31

for line in matrix:
    print(line)


print(count)


#WRONG: 77, 83 CORRECT 211