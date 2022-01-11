#!/usr/bin/python3

### DAY 4.1
with open('test.txt', 'r') as f:
    clean_input = []
    add_grid = []
    for line in f:
        if ',' in line:
            drawn_numbers = line.strip().split(',')
        elif line is "\n":
            if bool(add_grid) is True:
                clean_input.append(add_grid)
                add_grid = []
        else:
            add_grid.append(line.strip().split())
    else:
        clean_input.append(add_grid)

    print(drawn_numbers)
    print(clean_input)


    f.close()
