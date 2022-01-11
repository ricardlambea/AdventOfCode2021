#!/usr/bin/python3

### DAY 10.1

f = open('input.txt','r')
input = [list(line.strip()) for line in f.readlines()]
# [ print(line) for line in input ]

start_list=['(','[','{','<']
end_list=[')',']','}','>']
start_dict={'(':0,'[':1,'{':2,'<':3}
end_dict={')':0,']':1,'}':2,'>':3}
score=0
punctuations={')':3,']':57,'}':1197,'>':25137}
start_stack, start_i_stack=[],[]
end_stack, end_i_stack=[],[]

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
            score+=punctuations[end_stack[-1]]
            start_stack.pop()
            end_stack.pop()
            break
print(score)

f.close()





