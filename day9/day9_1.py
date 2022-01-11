#!/usr/bin/python3

### DAY 9.1

f = open('input.txt','r')
input = [list(line.strip()) for line in f.readlines()]
# [ print(line) for line in input ]

lowest_numbers = []

for x in range(len(input)): # linia
    c_row = input[x]
    # print('current row ' + str(c_row))
    if x == 0:
        i_up, i_down = None, x + 1
    elif x == len(input)-1:
        i_up = x - 1
        i_down = None
    else:
        i_up = x - 1
        i_down = x + 1
    # print('up and down: ' + str(i_up), str(i_down))
    for y in range(len(c_row)): # columna dins cada linia
        c_col = input[x][y]
        # print('current number: ' + str(c_col))

        if y == 0:
            i_left, i_right = None, y + 1
        elif y == len(c_row)-1:
            i_left, i_right = y - 1, None
        else:
            i_left, i_right = y - 1, y + 1
        # print('left and right: ' + str(i_left), str(i_right))

        if i_up is None:
            up = None
            down = input[i_down][y]
            if i_left is None:
                left = None
                right = input[x][i_right]
            elif i_right is None:
                right = None
                left = input[x][i_left]
            else:
                left = input[x][i_left]
                right = input[x][i_right]

        elif i_down is None:
            down = None
            up = input[i_up][y]
            if i_left is None:
                left = None
                right = input[x][i_right]
            elif i_right is None:
                right = None
                left = input[x][i_left]
            else:
                left = input[x][i_left]
                right = input[x][i_right]

        elif i_right is None:
            right = None
            left = input[x][i_left]
            if i_up is None:
                up = None
                down = input[i_down][y]
            elif i_down is None:
                down = None
                up = input[i_up][y]
            else:
                up = input[i_up][y]
                down = input[i_down][y]

        elif i_left is None:
            left = None
            right = input[x][i_right]
            if i_up is None:
                up = None
                down = input[i_down][y]
            elif i_down is None:
                down = None
                up = input[i_up][y]
            else:
                up = input[i_up][y]
                down = input[i_down][y]

        else:
            up = input[i_up][y]
            down = input[i_down][y]
            left = input[x][i_left]
            right = input[x][i_right]

        if all(i > c_col for i in [up, down, left, right] if i is not None):
            # print('appending number ' + str(c_col) + ' to list...')
            lowest_numbers.append(c_col)

risk_levels = [int(i) + 1 for i in lowest_numbers]
final_risk = sum(risk_levels)
print(final_risk)

f.close()