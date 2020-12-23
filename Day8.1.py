file1 = open('PuzzleInput8.txt', 'r')
input = file1.readlines()

accumulator = 0
i = 0
program = []
for line in input:
    line = line.strip().rstrip()
    program.append(line)

hit_index = []

while i < len(program) - 1:
    print(program[i])
    if(i in hit_index):
        break
    hit_index.append(i)
    if(program[i][:3] == "nop"):
        i += 1
        next
    elif(program[i][:3] == "jmp"):
        modify = int(program[i][3:])
        print(modify)
        i += modify
        next
    elif(program[i][:3] == "acc"):
        modify = int(program[i][3:])
        print(modify)
        accumulator += modify
        i += 1
        next

print("Total: {}".format(accumulator))

# 2051 correct