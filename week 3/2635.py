first = int(input())
n = 0
answer = []

for i in range(first+1):
    answer_list = [first, i]
    j = 0
    while True:
        temp = answer_list[j] - answer_list[j+1]
        j += 1
        if temp < 0:
            break
        answer_list.append(temp)
        if n < len(answer_list):
            n = len(answer_list)
            answer = answer_list[:]

print(n)
print(*answer)