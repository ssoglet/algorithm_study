from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pos_list = list(map(int, input().split()))
deque = deque([i for i in range(1, n+1)])

count = 0
for i in pos_list:
    while True:
        if deque[0] == i:
            deque.popleft()
            break
        else:
            if deque.index(i) < len(deque)/2:
                while deque[0] != i:
                    deque.append(deque.popleft())
                    count += 1
            else:
                while deque[0] != i:
                    deque.appendleft(deque.pop())
                    count += 1

print(count)