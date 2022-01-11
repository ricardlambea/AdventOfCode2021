#!/usr/bin/python3

### DAY 10.2

f = open('input.txt','r')
input = [list(line.strip()) for line in f.readlines()]
# [ print(line) for line in input ]

start_list=['(','[','{','<']
end_list=[')',']','}','>']
start_dict={'(':0,'[':1,'{':2,'<':3}
end_dict={')':0,']':1,'}':2,'>':3}
score=0
punctuations={'(':1,'[':2,'{':3,'<':4}
start_stack=[]
end_stack=[]
incomplete_lines=[]

for line in input:
    for x in line:
        if x in start_list:
            start_stack.append(x)
        elif x in end_list:
            end_stack.append(x)
        if bool(start_stack) == bool(end_stack) and start_dict[start_stack[-1]] == end_dict[end_stack[-1]]:
            start_stack.pop()
            end_stack.pop()
        elif bool(start_stack) == bool(end_stack) and start_dict[start_stack[-1]] != end_dict[end_stack[-1]]:
            start_stack=[]
            end_stack=[]
            break
    # print(start_stack)
    incomplete_lines.append(start_stack)
    start_stack=[]
    end_stack=[]

final_scores = []
for x in incomplete_lines:
    if x:
        x.reverse()
        for y in x:
            score *= 5
            score += punctuations[y]
        final_scores.append(score)
        score=0
final_scores.sort()
print(final_scores[int(len(final_scores)/2-0.5)])
f.close()