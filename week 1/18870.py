n = int(input())
n_list = list(map(int, input().split()))

n_sorted = list(set(n_list))
n_sorted.sort()

n_order = {n_sorted[i]:i for i in range(len(n_sorted))}

for i in n_list:
    print(n_order[i], end=' ')