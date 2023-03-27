n = int(input())
judge_list = []

for i in range(n):
    judge_list.append(list(input().split()))

judge_list.sort(key=lambda x: int(x[0]))
for i in range(n):
    print(int(judge_list[i][0]), judge_list[i][1])