#!/usr/bin/python3

### DAY 6.1

with open('input.txt','r') as f:
    input_list = [int(i) for i in f.readlines()[0].strip().split(',')]
    print(input_list)

    ### TEST INPUT
    # input_list = [3,4,3,1,2]

    for day in range(0, 256):
        # print(input_list)
        for i in range(0, len(input_list)):
            if input_list[i] == 0:
                input_list.pop(i)
                input_list.insert(i, 6)
                input_list.append(8)
                continue
            c_fish = input_list[i]
            mod_fish = c_fish - 1
            input_list.pop(i)
            input_list.insert(i, mod_fish)
            print('its day: ' + str(day))
    # print(input_list)
    print(len(input_list))
    f.close()