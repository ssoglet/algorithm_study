import sys
input = sys.stdin.readline

n = int(input())
std_list = []

for i in range(n):
    w, h = map(int, input().split())
    std_list.append((w, h))

for i in std_list:
    rank = 1
    for j in std_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")