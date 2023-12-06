def cal(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])


N = int(input())
arr = list(map(int, input().split()))
cal(arr)
print(*arr)