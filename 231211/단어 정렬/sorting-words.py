n = int(input())
arr = []
for _ in range(n):
    tmp = input()
    arr.append(tmp)


arr2 = sorted(arr)
for i in range(n):
    print(arr2[i])