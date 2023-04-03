from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
pizza = list(map(int, input().split()))
temp = [0 for i in range(n)]
deque = deque()

for i in range(n):
    deque.append([i, 0])

count = 0

while deque:
    num, get = deque.popleft()
    count += 1
    get += 1
    
    if pizza[num] == get:
        temp[num] = count
    else:
        deque.append([num, get])

temp = map(str, temp)
print(' '.join(temp))