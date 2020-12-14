file1 = open('PuzzleInput6.txt', 'r')
input = file1.readlines()



alphabet_string = "abcdefghijklmnopqrstuvwxyz"
alphabet = list(alphabet_string)

current_answers = ""
total_current_answers = ""
first_answer_set = False
total_current_set = False
current_aswer_valid = True
total = 0

for answer in input:
    answer = answer.strip()
    if(answer == ''):
        print("--result--")
        print(total_current_answers)
        
        count = 0
        for letter in total_current_answers:
            count += 1
        print(count)
        total += count
        print ("-----------")
        current_answers = ""
        total_current_answers = ""
        first_answer_set = False
        total_current_set = False
    else:        
        print(answer)
        if(first_answer_set is False):
            total_current_answers = answer
            first_answer_set = True
            current_aswer_valid = True
        for letter in total_current_answers:
            if(letter not in answer):
                total_current_answers = total_current_answers.replace(letter, "")


print("--result--")
print(total_current_answers)

count = 0
for letter in total_current_answers:
    count += 1
print(count)
total += count
print("-----------")
print("---Total---")
print(total)

#3353 too high/ 3294 too high/ correct: 3288