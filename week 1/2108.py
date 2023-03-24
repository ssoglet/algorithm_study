from collections import Counter
n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))

total = 0
for i in range(n):
    total += num_list[i]
avg = round(total/n)
print(avg)

num_list_sort = sorted(num_list)
print(num_list_sort[n//2])

count = Counter(num_list)
mode = count.most_common()
if len(count) == 1:
    print(mode[0][0])
else:
    if mode[0][1] == mode[1][1]:
        mode_list = []
        for i in range(len(mode)):
            if mode[0][1] == mode[i][1]:
                mode_list.append(mode[i][0])
        mode_list.sort()
        print(mode_list[1])
    else:
        print(mode[0][0])

print(num_list_sort[n-1]-num_list_sort[0])