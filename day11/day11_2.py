#!/usr/bin/python3

### DAY 11.2

def increaseEnergy(x, y, matrix):
    bottomBound = len(matrix)
    rightBound = len(matrix[0])
    if matrix[x][y] >= 10:
        matrix[x][y] = 0
        if x-1 >= 0: # UP
            if matrix[x-1][y] < 10 and matrix[x-1][y] != 0:
                matrix[x-1][y] += 1
        if y+1 < rightBound and x-1 >= 0: # UP-Right
            if matrix[x-1][y+1] < 10  and matrix[x-1][y+1] != 0:
                matrix[x-1][y+1] += 1
        if y+1 < rightBound: # RIGHT
            if matrix[x][y+1] < 10  and matrix[x][y+1] != 0:
                matrix[x][y+1] += 1
        if y+1 < rightBound and x+1 < bottomBound: # DOWN-Right
            if matrix[x+1][y+1] < 10 and matrix[x+1][y+1] != 0:
                matrix[x+1][y+1] += 1
        if x+1 < bottomBound: # DOWN
            if matrix[x+1][y] < 10 and matrix[x+1][y] != 0:
                matrix[x+1][y] += 1
        if y-1 >= 0 and x+1 < bottomBound: # DOWN-LEFT
            if matrix[x+1][y-1] < 10 and matrix[x+1][y-1] != 0:
                matrix[x+1][y-1] += 1
        if y-1 >= 0: # LEFT
            if matrix[x][y-1] < 10 and matrix[x][y-1] != 0:
                matrix[x][y-1] += 1
        if x-1 >= 0 and y-1 >= 0: # UP-LEFT
            if matrix[x-1][y-1] < 10 and matrix[x-1][y-1] != 0:
                matrix[x-1][y-1] += 1
    return matrix

import numpy as np
f = open('input.txt', 'r')
grid = np.array([list(map(int, line.strip())) for line in f])
f.close()
flashes = 0
stepFlashes = 0
steps = 100
step = 0
totalOctopuses = len(grid) * len(grid[0])
while True:
    grid += 1
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            grid = increaseEnergy(row, column, grid)

    tens = [(r, c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == 10] #store the coords for the positions where there is a 10
    while tens:
        for i,j in tens:
            grid = increaseEnergy(i,j, grid)
        tens = [(r, c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == 10]

    stepFlashes = len([(r, c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == 0]) #count how many positions are 0 after increasing all the possible energies
    step += 1
    if step < 100:
        flashes += stepFlashes
    if stepFlashes == totalOctopuses:
        break
print('All octopuses flash at: ', step)
print('Flashes:', flashes)