#!/usr/bin/python3

### DAY 1.1

with open("/home/ricard/Escritorio/AoC_2021/day1_1/input.txt",'r') as f:
    i = 0
    prev_line = 1000000000
    for line in f:
        if int(line.strip()) > prev_line:
            i += 1
            prev_line = int(line.strip())
        else:
            prev_line = int(line.strip())

    print(i)
    f.close()
