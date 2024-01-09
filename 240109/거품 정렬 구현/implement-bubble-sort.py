n = int(input())

arr = list(map(int, input().split()))

for i in range(len(arr)):
    for k in range(len(arr)-1):
        if arr[k] > arr[k+1]:
            tmp = arr[k]
            arr[k] = arr[k+1]
            arr[k+1] = tmp

print(*arr)