#!/usr/bin/python3

### DAY 7.2

def sumatorial(m):
    return int((m**2 + m) / 2)

# test = [16,1,2,0,4,2,7,1,2,14]
f = open('input.txt','r')
test = [int(i) for i in f.readlines()[0].strip().split(',')]

h_pos = {}
for i in test:
    if i not in h_pos:
        h_pos.setdefault(i, 1)
    else:
        h_pos[i] += 1
# print(h_pos)

total_fuel = 0
all_fuels = {}
for n in range(len(test) + 1): # for each possible final position
    for j in h_pos: # for each initial position
        steps = abs(n - j)
        fuel = sumatorial(steps) # fuel used by one submarine in that position
        all_submarines_with_same_key = fuel * h_pos[j] # fuel used by all submarines in that position
        total_fuel += all_submarines_with_same_key # total fuel used in that final position
    # print('final position ' + str(n) + ':')
    # print(total_fuel)
    all_fuels[n] = total_fuel
    total_fuel = 0
print(min(all_fuels.values()))

f.close()
