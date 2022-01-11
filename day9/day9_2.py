#!/usr/bin/python3

### DAY 9.2

def find_lowest_points(input):
    lowest_numbers = []
    lowest_numbers_coords = []

    for x in range(len(input)):  # linia
        c_row = input[x]
        # print('current row ' + str(c_row))
        if x == 0:
            i_up, i_down = None, x + 1
        elif x == len(input) - 1:
            i_up = x - 1
            i_down = None
        else:
            i_up = x - 1
            i_down = x + 1
        # print('up and down: ' + str(i_up), str(i_down))
        for y in range(len(c_row)):  # columna dins cada linia
            c_col = input[x][y]
            # print('current number: ' + str(c_col))

            if y == 0:
                i_left, i_right = None, y + 1
            elif y == len(c_row) - 1:
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
                lowest_numbers.append(c_col) # we store the lowest number (useful in the first part of the problem)
                lowest_numbers_coords.append((x,y)) # we store the coords of the lowest numbers
    return lowest_numbers_coords

def find_basin(lowest_numbers_coords, input):
    sizes = []
    for x,y in lowest_numbers_coords:
        sizes.append(check_point(x, y, input)) # for each lowest number check how big the basin it belongs to is
    return sizes

def check_point(x, y, input):
    size = 0
    if (x >= 0
        and y >= 0
        and y < len(input)
        and x < len(input[y])):
        if input[y][x] != '.' and input[y][x] < 9:
            input[y][x] = '.'
            size = 1
            size += check_point(x+1, y, input)
            size += check_point(x-1, y, input)
            size += check_point(x, y+1, input)
            size += check_point(x, y-1, input)
    return size


def get_basin_size(points_location, input):
    first = 0
    second = 0
    third = 0
    for point in points_location:
        size = check_point(point[0], point[1], input)
        if size > first:
            third = second
            second = first
            first = size
        elif size > second:
            third = second
            second = size
        elif size > third:
            third = size
    return first, second, third, first * second * third

if __name__ == "__main__":
    f = open('input.txt','r')
    # input = [list(line.strip()) for line in f.readlines()]
    input = []
    for line in f:
        input.append(list(map(int, list(line.replace('\n', '')))))
    lowest_numbers_coords = find_lowest_points(input)
    basin_sizes = find_basin(lowest_numbers_coords, input)
    top3_basins = sorted(basin_sizes)[::-1][0:3]
    print(top3_basins, top3_basins[0]*top3_basins[1]*top3_basins[2])

    f.close()
