#!/usr/bin/python3

### DAY 14.2

'''
First line is the polymer template.
From the second to last line, there are the pair insertion rules. A rule like NN -> H means that if NN is found, H is inserted in between.
The second element of one pair will be the first element for the next pair to parse.
Inserted elements are not considered to be part of an insertion pair until the following step.
Find the most and least common elements after 10 steps and substract the second to the first. This number is the answer.
'''

from collections import Counter #subclass of the dictionary class
from functools import lru_cache #this module helps in reducing the execution time of the function it is decorating
from datetime import datetime

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

# this function was partly taken from the AoC subreddit as my answer was not optimal and the execution time grew up to infinite
def grow_polymer(template, rules, max_steps):
    @lru_cache(maxsize=None)
    def count(pair, step):
        if step == max_steps or pair not in rules:
            return Counter()
        step += 1
        new_element = rules[pair]
        new_counter = Counter(new_element)
        new_counter.update(count(pair[0] + new_element, step))
        new_counter.update(count(new_element + pair[1], step))
        return new_counter

    counter = Counter(template)
    for left, right in zip(template, template[1:]):
        counter.update(count(left + right, 0))
    return counter


startTime = datetime.now()

f = open('input.txt','r')
polymer, rules = parse_file(f)
f.close()
steps = 40
counts = grow_polymer(polymer, rules, steps)
max_value, min_value = counts.most_common()[0][1], counts.most_common()[-1][1]

print('Answer is:', max_value-min_value)
print(datetime.now() - startTime)



