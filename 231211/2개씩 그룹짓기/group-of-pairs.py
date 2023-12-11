n = int(input())
a = list(map(int, input().split()))

aa = sorted(a)
bb = list(reversed(aa))


for i in range(n):
    max = 0
    now = aa[i] + bb[i]
    if now > max:
        max = now

print(max)