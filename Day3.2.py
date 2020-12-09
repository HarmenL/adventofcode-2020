file1 = open('PuzzleInput3.txt', 'r') 
Lines = file1.readlines()

y = len(Lines)
x = len(Lines[0])

print(x)
print(y)
matrix = [[0 for i in range(x)] for i in range(y)] 

def split(word):
    word = word.rstrip("\n")
    return [char for char in word]

index = 0
for read_line in Lines:
    split_line = split(read_line)
    matrix[index] = split_line
    index += 1

def count_tree(step_x, step_y) :
    count = 0
    index_x = 0
    index_y = 0
    while (index_y < 323) :
        value_found = matrix[index_y][index_x]
        if(value_found == '#'):
            count += 1
        index_y += step_y
        index_x += step_x
        print("X:{} Y:{}".format(index_x, index_y))
        if(index_x >= 31):
            index_x -= 31

    return count


tree_1 = count_tree(1, 1)
tree_2 = count_tree(3, 1)
tree_3 = count_tree(5, 1)
tree_4 = count_tree(7, 1)
tree_5 = count_tree(1, 2)

print(tree_1 * tree_2 * tree_3 * tree_4 * tree_5)


#WRONG: 77, 83 CORRECT 211

# ANSWER: 3584591857