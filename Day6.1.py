file1 = open('PuzzleInput6.txt', 'r')
input = file1.readlines()



alphabet_string = "abcdefghijklmnopqrstuvwxyz"
alphabet = list(alphabet_string)

current_answers = ""
total = 0

for answer in input:
    answer = answer.strip()
    if(answer == ''):
        print("--result--")
        count = 0
        for letter in alphabet:
            if(letter in current_answers):
                count += 1
        print(count)
        total += count
        print("-----------")
        current_answers = ""
    else:
        current_answers += answer
        print(answer)

print("--result--")
count = 0
for letter in alphabet:
    if(letter in current_answers):
        count += 1
print(count)
total += count
print("-----------")
current_answers = ""
print("---Total---")
print(total)

#6340 too low