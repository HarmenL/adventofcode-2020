file1 = open('PuzzleInput5.txt', 'r')
input = file1.readlines()

highest_id = 0

for board_pass in input:
    board_pass = board_pass.replace('F', '0').rstrip()
    board_pass = board_pass.replace('R', '1')
    board_pass = board_pass.replace('B', '1')
    board_pass = board_pass.replace('L', '0')

    row = int(board_pass[0:7], 2)
    column = int(board_pass[7:10], 2)
    id = row * 8 + column
    if(id > highest_id):
        highest_id = id

print(highest_id)

#correct: 850