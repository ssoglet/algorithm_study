import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = []

for i in range(n):
    num.append(list(input()))

temp = min(n,m)
answer = 0

for i in range(n):
    for j in range(m):
        for k in range(temp):
            if ((i+k)<n) and ((j+k)<m) and (num[i][j] == num[i][j+k] == num[i+k][j] == num[i+k][j+k]):
                answer = max(answer, (k+1)**2)

print(answer)