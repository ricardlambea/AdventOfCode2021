#!/usr/bin/python3

### DAY 8.1
# no he entes el problema xd

f = open('test.txt','r')
input = [line.strip().split('|')[1].lstrip(' ') for line in f.readlines()]
print(input)

f.close()