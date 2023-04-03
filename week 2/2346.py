import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deque = deque(enumerate(map(int, input().split())))
answer = []

while deque:
    idx, paper = deque.popleft()
    answer.append(idx+1)

    if paper > 0:
        deque.rotate(-(paper-1))
    elif paper < 0:
        deque.rotate(-paper)

print(' '.join(map(str, answer)))