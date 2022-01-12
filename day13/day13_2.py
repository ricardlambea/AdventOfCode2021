#!/usr/bin/python3

### DAY 13.2

''' First value x increases to the right. Second value y increases downward.
# represents a dot in the paper and . represents an empty position.
Fold along y=4 tells us to fold the bottom part upwards at line 4.'''

def parse_file(f):
    folds = []
    max_x, max_y = 0, 0
    coords = []
    for line in f.readlines():
        if line.startswith('fold along'):
            folds.append(line.strip().split(' ')[2])
        elif line == '\n':
            continue
        else:
            x = int(line.strip().split(',')[0])
            y = int(line.strip().split(',')[1])
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            coords.append((x, y))
    return coords, folds, max_x, max_y

def create_grid(y, x):
    grid = []
    for i in range(y+1):
        grid.append(['.' for _ in range(x+1)])
    return grid

def print_dots(coords,grid):
    for x, y in coords:
        grid[y][x] = '#'
    return grid

def fold_grid(fold, grid):
    if 'y' in fold:
        n = int(fold.split('=')[1])
        c_grid = grid[:n]
        subgrid = grid[n+1:]
        for i in range(len(subgrid)):
            for j in range(len(subgrid[0])):
                if subgrid[i][j] == '#':
                    c_grid[-i-1][j] = '#'
    elif 'x' in fold:
        n = int(fold.split('=')[1])
        c_grid = [line[:n] for line in grid]
        subgrid = [line[n+1:] for line in grid]
        for i in range(len(subgrid)):
            for j in range(len(subgrid[0])):
                if subgrid[i][j] == '#':
                    c_grid[i][-j-1] = '#'
    return c_grid


if __name__ == "__main__":
    f = open('input.txt','r')
    coords, folds, max_x, max_y = parse_file(f)
    grid = create_grid(max_y, max_x)
    grid = print_dots(coords, grid)
    while folds:
        fold = folds.pop(0)
        grid = fold_grid(fold, grid)

    print('The code is:')
    [print(''.join(line)) for line in grid]

    f.close()

