import sys

n = int(input())
stack = []
answer = []
flag = False
temp = 1

for i in range(n):
    num = int(sys.stdin.readline())
    while temp <= num:
        stack.append(temp)
        answer.append("+")
        temp += 1
    
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = True
        break

if not flag:
    for i in range(len(answer)):
        print(answer[i])