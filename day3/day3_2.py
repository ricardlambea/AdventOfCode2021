#!/usr/bin/python3

### DAY 3.2
import numpy as np

with open('input.txt','r') as f:
    input_list = np.loadtxt(f, dtype=str)
    ones_list = []
    zeros_list =[]

    for i in range(0, len(input_list[0])):
        # print('iteration: ' + str(i+1))
        # print(input_list)
        for number in input_list:
            if number[i] == '0':
                zeros_list.append(number)
            else:
                ones_list.append(number)
        # print('number of 0s: ' + str(len(zeros_list)))
        # print('number of 1s: ' + str(len(ones_list)))
        if len(zeros_list) > len(ones_list):
            input_list = zeros_list
        elif len(zeros_list) < len(ones_list):
            input_list = ones_list
        else:
            input_list = ones_list
        if len(input_list) == 1:
            break
        zeros_list = []
        ones_list = []
    print('final number:\t' + input_list[0])
    o2_rate = str(int(input_list[0], 2))
    print('oxygen rate in decimal is: ' + o2_rate)
    f.close()


with open('input.txt','r') as f:
    input_list = np.loadtxt(f, dtype=str)
    ones_list = []
    zeros_list =[]

    for i in range(0, len(input_list[0])):
        # print('iteration: ' + str(i+1))
        # print(input_list)
        for number in input_list:
            if number[i] == '0':
                zeros_list.append(number)
            else:
                ones_list.append(number)
        # print('number of 0s: ' + str(len(zeros_list)))
        # print('number of 1s: ' + str(len(ones_list)))
        if len(zeros_list) < len(ones_list):
            input_list = zeros_list
        elif len(zeros_list) > len(ones_list):
            input_list = ones_list
        else:
            input_list = zeros_list
        if len(input_list) == 1:
            break
        zeros_list = []
        ones_list = []
    print('final number:\t' + input_list[0])
    co2_rate = str(int(input_list[0], 2))
    print('co2 rate in decimal is: ' + co2_rate)

    f.close()

print('the final result is: ' + str(int(o2_rate) * int(co2_rate)))
