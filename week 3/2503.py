from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
num = list(permutations([1,2,3,4,5,6,7,8,9],3))

for _ in range(n):
    test, s, b = map(int, input().split())
    test = list(str(test))
    remove = 0

    for i in range(len(num)):
        s_count, b_count = 0, 0
        i -= remove

        for j in range(3):
            test[j] = int(test[j])
            if test[j] in num[i]:
                if j == num[i].index(test[j]):
                    s_count += 1
                else:
                    b_count += 1

        if s_count != s or b_count != b:
            num.remove(num[i])
            remove += 1

print(len(num))