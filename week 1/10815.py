n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

def bi_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(m):
    if bi_search(n_list, m_list[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')