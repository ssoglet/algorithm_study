import heapq
import sys
input = sys.stdin.readline

heap = []
n = int(input())

for i in range(n):
    n_list = list(map(int, input().split()))
    if not heap:
        for num in n_list:
            heapq.heappush(heap, num)
    else:
        for num in n_list:
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)
            
print(heap[0])