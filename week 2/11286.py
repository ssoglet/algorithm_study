import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)