from collections import deque
import sys
input = sys.stdin.readline

deque = deque()
answer = []
n, k = map(int, input().split())

for i in range(1, n+1):
    deque.append(i)

while deque:
    for i in range(k-1):
        deque.append(deque.popleft())
    answer.append(deque.popleft())

print("<", end='')
for i in range(len(answer)-1):
    print("%d, "%answer[i], end='')
print(answer[-1], end='')
print(">")