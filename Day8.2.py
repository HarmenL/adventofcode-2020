file1 = open('PuzzleInput8.txt', 'r')
input = file1.readlines()

accumulator = 0
i = 0
program = []
nops = []
jmps = []
for line in input:
    line = line.strip().rstrip()
    program.append(line)
    if(program[i][:3] == "nop"):
        nops.append(i)
    elif(program[i][:3] == "jmp"):
        jmps.append(i)
    i += 1
    

hit_index = []

finished = False

nops_index = 0
jmps_index = 0
while finished is False:
    i = 0
    looped = False
    accumulator = 0
    hit_index.clear()
    if(len(nops) > 0):
        nop_index = nops.pop()
        new_program = program.copy()
        new_program[nop_index] = new_program[nop_index].replace("nop", "jmp")
    elif(len(jmps) > 0):
        jmp_index = jmps.pop()
        new_program = program.copy()
        new_program[jmp_index] = new_program[jmp_index].replace("jmp", "nop")
        print(new_program)





    while i < len(new_program):
        print(new_program[i])
        if(i in hit_index):
            looped = True
            break
        hit_index.append(i)
        if(new_program[i][:3] == "nop"):
            i += 1
            next
        elif(new_program[i][:3] == "jmp"):
            modify = int(new_program[i][3:])
            print(modify)
            i += modify
            next
        elif(new_program[i][:3] == "acc"):
            modify = int(new_program[i][3:])
            print(modify)
            accumulator += modify
            i += 1
            next
    if(looped != True):
        finished = True
    print("Finished loop.")

print("Total: {}".format(accumulator))

# 2051 correct