def cal(arr):
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[i] //= 2
    return arr

N = int(input())
arr = list(map(int, input().split()))
print(*cal(arr))