file1 = open('PuzzleInput5.txt', 'r')
input = file1.readlines()

ids = []

for board_pass in input:
    board_pass = board_pass.replace('F', '0').rstrip()
    board_pass = board_pass.replace('R', '1')
    board_pass = board_pass.replace('B', '1')
    board_pass = board_pass.replace('L', '0')

    row = int(board_pass[0:7], 2)
    column = int(board_pass[7:10], 2)
    id = row * 8 + column
    ids.append(id)

ids.sort()
i = 0
while i < len(ids) - 1:
    if(ids[i] + 1 != ids[i + 1]):
        print("Missing seat id:{}".format(ids[i] + 1))
    i += 1

#answer: 598 to low/ 599 correct