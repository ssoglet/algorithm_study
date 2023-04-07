import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input()) for _ in range(n)]
answer = 0

def check(arr):
    n = len(arr)
    answer = 1

    for i in range(n):
        count = 1
        for j in range(1,n):
            if arr[j][i] == arr[j-1][i]:
                count += 1
            else:
                count = 1
            if count > answer:
                answer = count

        count = 1
        for j in range(1,n):
            if arr[i][j] == arr[i][j-1]:
                count += 1
            else:
                count = 1
            if count > answer:
                answer = count
    
    return answer

for i in range(n):
    for j in range(n):
        if i+1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            temp = check(arr)
            if temp > answer:
                answer = temp
            arr[i][j], arr[i+1][j]= arr[i+1][j], arr[i][j]

        if j+1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            temp = check(arr)
            if temp > answer:
                answer = temp
            arr[i][j], arr[i][j+1]= arr[i][j+1], arr[i][j]
        
print(answer)