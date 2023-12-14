n = int(input())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0
for i in range(n):
    r, d = map(str, input().split())
    d = int(d)
    if r == 'E':
        rn = 0
    elif r == 'S':
        rn = 1
    elif r == 'W':
        rn = 2
    else:
        rn = 3

    for k in range(d):
        x, y = x+dx[rn], y+dy[rn]

print(x, y)