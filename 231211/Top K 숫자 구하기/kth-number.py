n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = sorted(arr)

print(arr2[k-1])