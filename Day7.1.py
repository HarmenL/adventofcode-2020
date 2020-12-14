
def checkbag (bag):
    if(bag in bag_infos):

        bag_info = bag_infos[bag]
        bag_info_split = bag_info.split(',')
        return_value = False
        for split in bag_info_split:
            if("shiny gold" in split):
                return_value = True
            elif("other" in split):
                a = 1
            else:
                value = checkbag(split)
                if(value == True):
                    return_value = True
        return return_value
    else:
        return False

file1 = open('PuzzleInput7.txt', 'r')
input = file1.readlines()
y = len(input)
bag_infos = { }

count = 0
for line in input:

    #print("-------------------------------")
    bag = line.split("contain")[0].replace("bags", "").replace("bag", "").strip()
    #print(bag)
    #print("-")
    info = line.split("contain")[1].replace("bags", "").replace("bag", "").split(",")
    info_count = 0
    bag_info = ""
    for baginfo in info:
        baginfo = baginfo.replace(".", "")
        baginfo = baginfo[1:]
        #print(baginfo)
        bag_info += baginfo[2:].rstrip() + ","
        info_count += 1
    bag_infos.update({bag: bag_info[:-1]})
    count += 1

count = 0
i = 0
for key in bag_infos:
    
    print("-------------------------------")
    print(key)
    print("-")
    print(bag_infos[key])
    i += 1
    
print("-------------------------------")
print(len(bag_infos))
bag_count = 0
i = 0
bags_checked_count = 0
print("-------------------------------")
for key in bag_infos:
    if(key is not "shiny gold"):       
        check = checkbag(key)
        if(check == True):
            bag_count += 1
            print(key)
        bags_checked_count += 1
print(bag_count)  
print(bags_checked_count)
# while i < len(bag_infos) - 1:

#     check = checkbag(bag_infos[i])
#     if(check == True):
#         bag_count += 1
#     i += 1
#     # j = 0
#     # print("-------------------------------")
#     # print(bag_infos[i])
#     # print("-")
#     # while j < len(bag_infos[i]) - 1:
#     #     bag = bag_infos[i][j]
#     #     if(bag not is "no other"):

#     #     print(bag_infos[i][j])

#     #     j += 1
#     # i += 1

# print(bag_count)


# wrong 13 wrong 46 wrong 144 too low wrong 145 wrong 250 correct 222