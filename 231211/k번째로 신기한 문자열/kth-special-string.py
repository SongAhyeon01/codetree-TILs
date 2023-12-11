n, k, T = input().split()
n = int(n)
k = int(k)
s = len(T)


arr = []
for _ in range(n):
    tmp = input()
    arr.append(tmp)

so = []
for j in arr:
    if j[:s] == T:
        so.append(j)

so.sort()

print(so[k-1])