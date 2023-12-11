n = int(input())
arr = [*map(int, input().split())]

arr1 = sorted(arr)
arr2 = list(reversed(arr1))
print(*arr1)
print(*arr2)