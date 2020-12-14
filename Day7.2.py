


def checkbag (bag, parent_value):
    return_value = ""
    bag_info = bag_infos[bag]
    bag_info_split = bag_info.split(',')
    for split in bag_info_split:
        bag_value = split[0]
        if("other" not in split):
            split = split[2:]
            result = checkbag(split, "{} * {}".format(parent_value, bag_value))
            return_value += result
        else:  
            return_value += ""
    return "{} + {}".format(parent_value, return_value)
file1 = open('PuzzleInput7.txt', 'r')
input = file1.readlines()
y = len(input)
bag_infos = { }
total = ""
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
        bag_info += baginfo.rstrip() + ","
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
print("-------------------------------")

for key in bag_infos:
    if("shiny gold" in key):       
        total = checkbag("drab gray", 4)
        total += checkbag("light coral", 4)
        
print(total)

total = total.replace("+ +", "+").replace(" + *", "*")
print(total)
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


# too high 15746 too high 15745/ too high 15730/ correct: 13264