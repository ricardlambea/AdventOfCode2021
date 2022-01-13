#!/usr/bin/python3

### DAY 14.1

'''
First line is the polymer template.
From the second to last line, there are the pair insertion rules. A rule like NN -> H means that if NN is found, H is inserted in between.
The second element of one pair will be the first element for the next pair to parse.
Inserted elements are not considered to be part of an insertion pair until the following step.
Find the most and least common elements after 10 steps and substract the second to the first. This number is the answer.
'''

def parse_file(f):
    file = f
    rules = {}
    for line in file.readlines():
        if '->' not in line:
            if line == '\n':
                continue
            template = line.strip()
        else:
            pair = line.strip().split(' -> ')[0]
            inserted = line.strip().split(' -> ')[1]
            rules.setdefault(pair, inserted)
    return template, rules

def grow_polymer(polymer, rules):
    c_polymer = list(polymer)
    i=0
    while i < len(c_polymer)-1:
        c_pair = str(c_polymer[i]+c_polymer[i+1])
        if c_pair in rules:
            c_polymer.insert(i+1, rules[c_pair])
            i+=1
        i+=1
    polymer = ''.join(c_polymer)
    return polymer

def count_elements(polymer):
    counts = {}
    for element in polymer:
        if element not in counts.keys():
            count = polymer.count(element)
            counts[element] = count
    return counts


from datetime import datetime
startTime = datetime.now()

f = open('input.txt','r')
polymer, rules = parse_file(f)
f.close()
steps = 10
for n in range(steps):
    print(n)
    polymer = grow_polymer(polymer, rules)
counts = count_elements(polymer)
max_value, min_value = max(counts.values()), min(counts.values())

print('Answer is:', max_value-min_value)
print(datetime.now() - startTime)



