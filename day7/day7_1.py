#!/usr/bin/python3

### DAY 7.1

# test = [16,1,2,0,4,2,7,1,2,14]
f = open('input.txt','r')
input = [int(i) for i in f.readlines()[0].strip().split(',')]

fuel = []
for n in range(0, max(input) + 1):
    print(n)
    diffs = [abs(x - n) for x in input]
    fuel.append(sum(diffs))
print(min(fuel))

f.close()