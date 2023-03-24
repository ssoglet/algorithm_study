n = int(input())
num_list = [[0 for i in range(2)] for j in range(n)]

for i in range(n):
    x, y = input().split()
    num_list[i][0] = int(x)
    num_list[i][1] = int(y)

num_list.sort()
for x, y in num_list:
    print(x, y)