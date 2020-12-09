file1 = open('PuzzleInput4.txt', 'r')
Lines = file1.readlines()

passport_checks = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

eye_checks = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

current_passport = ""
passports = []
for read_line in Lines:
    if(read_line == "\n"):
        passports.append(current_passport.rstrip())
        current_passport = ""
    else:
        current_passport += read_line.replace("\n", " ")
passports.append(current_passport.rstrip())

count_valid = 0
for passport in passports:
    valid = True
    for check in passport_checks:
        if(check not in passport):
            valid = False
    if(valid == True):
        fields = passport.split(' ')
        for field in fields:
            field_parts = field.split(':')
            title = field_parts[0]
            value = field_parts[1]
            if(title == "byr"):
                value = int(value)
                if(value < 1920 or value > 2002):
                    valid = False
            elif(title == "iyr"):
                value = int(value)
                if(value < 2010 or value > 2020):
                    valid = False
            elif(title == "eyr"):
                value = int(value)
                if(value < 2020 or value > 2030):
                    valid = False
            
            elif(title == "hgt"):
                if("cm" in value):
                    value = int(value.strip("cm"))
                    if(value < 150 or value > 193):
                        valid = False
                elif("in" in value):
                    value = int(value.strip("in"))
                    if(value < 59 or value > 76):
                        valid = False
                else:
                    valid = False

            elif(title == "hcl"):
                if(value[0] == "#"):
                    value = value.strip("#")
                    if(len(value) == 6) :
                        for c in value:
                            if(c not in "0123456789abcdef"):
                                valid = False
                    else:
                        valid = False
                else:
                    valid = False
            elif(title == "ecl"):
                eye_valid = False
                for eye_check in eye_checks:
                    if(value == eye_check):
                        eye_valid = True
                if(eye_valid == False):
                    valid = False
            elif(title == "pid"):
                if(len(value) == 9) :
                    for c in value:
                        if(c not in "0123456789"):
                            valid = False
                else:
                    valid = False
    if(valid):
        count_valid += 1
        print(passport)


print("Valid passports: {}".format(count_valid))

# 118 too high correct:114