#!/usr/bin/python3

### DAY 2.1

with open('input.txt','r') as f:
    i_forward = 0
    i_depth = 0
    aim = 0

    for line in f:
        direction = line.strip().split()[0]
        steps = int(line.strip().split()[1])
        if direction == 'forward':
            i_forward += steps
        elif direction == 'up':
            i_depth -= steps
        elif direction == 'down':
            i_depth += steps
    print(i_forward, i_depth)
    print(i_forward * i_depth)
    f.close()
