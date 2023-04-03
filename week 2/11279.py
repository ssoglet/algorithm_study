import sys
import heapq

n = int(input())
heap = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (-num, num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)