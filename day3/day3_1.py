#!/usr/bin/python3

### DAY 3.1

with open('input.txt','r') as f:
    zeros_pos1, ones_pos1 = 0, 0
    zeros_pos2, ones_pos2 = 0, 0
    zeros_pos3, ones_pos3 = 0, 0
    zeros_pos4, ones_pos4 = 0, 0
    zeros_pos5, ones_pos5 = 0, 0
    zeros_pos6, ones_pos6 = 0, 0
    zeros_pos7, ones_pos7 = 0, 0
    zeros_pos8, ones_pos8 = 0, 0
    zeros_pos9, ones_pos9 = 0, 0
    zeros_pos10, ones_pos10 = 0, 0
    zeros_pos11, ones_pos11 = 0, 0
    zeros_pos12, ones_pos12 = 0, 0

    for line in f:
        position1 = int(list(line.strip())[0])
        position2 = int(list(line.strip())[1])
        position3 = int(list(line.strip())[2])
        position4 = int(list(line.strip())[3])
        position5 = int(list(line.strip())[4])
        position6 = int(list(line.strip())[5])
        position7 = int(list(line.strip())[6])
        position8 = int(list(line.strip())[7])
        position9 = int(list(line.strip())[8])
        position10 = int(list(line.strip())[9])
        position11 = int(list(line.strip())[10])
        position12 = int(list(line.strip())[11])

        if position1 == 0:
            zeros_pos1 += 1
        else:
            ones_pos1 += 1
        if position2 == 0:
            zeros_pos2 += 1
        else:
            ones_pos2 += 1
        if position3 == 0:
            zeros_pos3 += 1
        else:
            ones_pos3 += 1
        if position4 == 0:
            zeros_pos4 += 1
        else:
            ones_pos4 += 1
        if position5 == 0:
            zeros_pos5 += 1
        else:
            ones_pos5 += 1
        if position6 == 0:
            zeros_pos6 += 1
        else:
            ones_pos6 += 1
        if position7 == 0:
            zeros_pos7 += 1
        else:
            ones_pos7 += 1
        if position8 == 0:
            zeros_pos8 += 1
        else:
            ones_pos8 += 1
        if position9 == 0:
            zeros_pos9 += 1
        else:
            ones_pos9 += 1
        if position10 == 0:
            zeros_pos10 += 1
        else:
            ones_pos10 += 1
        if position11 == 0:
            zeros_pos11 += 1
        else:
            ones_pos11 += 1
        if position12 == 0:
            zeros_pos12 += 1
        else:
            ones_pos12 += 1
    final1 = '0' if zeros_pos1 > ones_pos1 else '1'
    final2 = '0' if zeros_pos2 > ones_pos2 else '1'
    final3 = '0' if zeros_pos3 > ones_pos3 else '1'
    final4 = '0' if zeros_pos4 > ones_pos4 else '1'
    final5 = '0' if zeros_pos5 > ones_pos5 else '1'
    final6 = '0' if zeros_pos6 > ones_pos6 else '1'
    final7 = '0' if zeros_pos7 > ones_pos7 else '1'
    final8 = '0' if zeros_pos8 > ones_pos8 else '1'
    final9 = '0' if zeros_pos9 > ones_pos9 else '1'
    final10 = '0' if zeros_pos10 > ones_pos10 else '1'
    final11 = '0' if zeros_pos11 > ones_pos11 else '1'
    final12 = '0' if zeros_pos12 > ones_pos12 else '1'

    gamma_rate = final1+final2+final3+final4+final5+final6+final7+final8+final9+final10+final11+final12
    print(gamma_rate)

    epsilon_rate = ''
    for char in gamma_rate:
        if char == '0':
            epsilon_rate += '1'
        else:
            epsilon_rate += '0'
    print(epsilon_rate)

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))
    f.close()
