n = int(input())
n_list = []

for i in range(n):
    num = int(input())
    n_list.append(num)

n_list.sort()

for i in range(n):
    print(n_list[i])