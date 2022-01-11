#!/usr/bin/python3

### DAY 1.2

with open('input.txt','r') as f:
    count = 0
    inputfile = [ int(x.strip()) for x in f.readlines()]
    while len(inputfile) > 3:
        firstitem = inputfile[0]
        seconditem = inputfile[1]
        thirditem = inputfile[2]
        fourthitem = inputfile[3]
        prev_depth = sum([firstitem, seconditem, thirditem])
        new_depth = sum([seconditem, thirditem, fourthitem])
        if new_depth > prev_depth:
            count += 1
        del inputfile[0]
    else:
        f.close()

    f.close()
    print(count)
