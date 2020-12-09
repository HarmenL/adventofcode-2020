file1 = open('PuzzleInput4.txt', 'r') 
Lines = file1.readlines()

passport_checks = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

current_passport = ""
passports = []
for read_line in Lines:
    if(read_line == "\n"):
        passports.append(current_passport)
        current_passport = ""
    else:
        current_passport += read_line.rstrip("\n")
passports.append(current_passport)

count_valid = 0
for passport in passports:
    valid = True
    for check in passport_checks:
        if(check not in passport):
            valid = False
    if(valid == True):
        count_valid += 1        
        print(passport)

print("Valid passports: {}".format(count_valid))

# 196 correct
