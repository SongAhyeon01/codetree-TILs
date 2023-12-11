n = int(input())
arr = list(map(int, input().split()))

for i in range(n+1):
    if i%2 != 0:
        tmp = arr[:i]
        tmp_s = sorted(tmp)
        print(tmp_s[i//2], end=' ')