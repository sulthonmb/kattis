import sys

first = True
set_sudoku_problem = True
size_sudoku = ''
row = 0
i = 0
j = 0
regionals = []

for line in sys.stdin:
    data = str(line).replace("\n", "")

    if first == True:
        size_sudoku = [int(x) for x in data.replace("\n", "").split(' ')]
        row = size_sudoku[0]
        sudoku_problem = [[0 for j in range(size_sudoku[1])] for i in range(size_sudoku[0])]
        first = False
        continue
    
    if row != 0:
        values = data.replace("\n", "").split(' ')
        j = 0
        
        for value in values:
            sudoku_problem[i][j] = value

            j += 1
        
        row -= 1
        i += 1

    elif len(data.split(' ')) != 1:
        regionals.append(data.split(' '))

def parse_position(position):
    current_position = position.replace("(", "")
    current_position = current_position.replace(")", "")
    return current_position.split(",")

def is_out_of_bound(x, y):
  try:
    value = sudoku_problem[x][y]
    return False
  except IndexError:
    return True
    # print("value doesnt exist")

def check_sudoku(sudoku_problem, position, value):
    current_x = int(position[0]) - 1 # 2
    current_y = int(position[1]) - 1 # 2

    x1 = current_x-1 # 1
    y1 = current_y-1 # 1

    x2 = current_x-1 # 1
    y2 = current_y # 2

    x3 = current_x # 2
    y3 = current_y-1 # 1

    x4 = current_x+1 # 3
    y4 = current_y+1 # 3

    x5 = current_x+1 # 3
    y5 = current_y # 2

    x6 = current_x # 2
    y6 = current_y+1 # 3

    x7 = current_x-1 # 1
    y7 = current_y+1 # 3

    x8 = current_x+1 # 3
    y8 = current_y-1 # 1

    if not is_out_of_bound(x1, y1) and sudoku_problem[x1][y1] == int(value):
        return False
    elif not is_out_of_bound(x2, y2) and sudoku_problem[x2][y2] == int(value):
        return False
    elif not is_out_of_bound(x3, y3) and sudoku_problem[x3][y3] == int(value):
        return False
    elif not is_out_of_bound(x4, y4) and sudoku_problem[x4][y4] == int(value):
        return False
    elif not is_out_of_bound(x5, y5) and sudoku_problem[x5][y5] == int(value):
        return False
    elif not is_out_of_bound(x6, y6) and sudoku_problem[x6][y6] == int(value):
        return False
    elif not is_out_of_bound(x7, y7) and sudoku_problem[x7][y7] == int(value):
        return False
    elif not is_out_of_bound(x8, y8) and sudoku_problem[x8][y8] == int(value):
        return False
    
    return True

def brute_force_sudoku(sudoku_problem, regionals):
    for regional in regionals:
        value = 1
        count_value = int(regional[0])
        positions = regional[1:]

        if count_value == 1:
            position = parse_position(positions[0])
            is_avail = check_sudoku(sudoku_problem, position, value)
            if is_avail:
                sudoku_problem[int(position[0]) - 1][int(position[1]) - 1] = value
                value += 1
            else:
        else:
            for position in positions:
                position = parse_position(position)
                is_avail = check_sudoku(sudoku_problem, position, value)
                if is_avail:
                    sudoku_problem[int(position[0]) - 1][int(position[1]) - 1] = value
                    value += 1

            # sudoku_problem[]
        print('regional', regional[1:])

brute_force_sudoku(sudoku_problem, regionals)
print('sudoku_problem', sudoku_problem)
print('regionals', regionals)