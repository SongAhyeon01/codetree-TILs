n = int(input())
a = list(map(int, input().split()))

aa = sorted(a)
bb = list(reversed(aa))

max = 0
for i in range(n):
    now = aa[i] + bb[i]
    if now > max:
        max = now

print(max)