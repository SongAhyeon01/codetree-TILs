n = int(input())

line = [0 for i in range(100)]

for _ in range(n):
    now = 50
    x, r = map(str, input().split())
    x = int(x)

    if r == 'R':
        for k in range(now, x, 1):
            line[k] += 1
            now = now + x
    else:
        for k in range(now, now-x, -1):
            line[k] += 1
            now = now - x


cnt = 0
for j in range(len(line)):
    if line[j] >= 2:
        cnt += 1

print(cnt)