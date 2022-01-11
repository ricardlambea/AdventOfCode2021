#!/usr/bin/python3

### DAY 2.2

with open('input.txt','r') as f:
    i_forward = 0
    i_depth = 0
    aim = 0

    for line in f:
        direction = line.strip().split()[0]
        steps = int(line.strip().split()[1])
        if direction == 'forward':
            i_forward += steps
            if aim == 0:
                continue
            else:
                i_depth += steps * aim
        elif direction == 'up':
            aim -= steps
        elif direction == 'down':
            aim += steps
    print(i_forward, i_depth)
    print(i_forward * i_depth)
    f.close()
