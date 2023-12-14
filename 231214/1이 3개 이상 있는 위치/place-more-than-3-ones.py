def in_range(x, y, n):
    return x >= 0 and x<n and y >=0 and y<n

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

total_cnt = 0
for x in range(len(a)):
    for y in range(len(a)):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, n) and a[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            total_cnt += 1

print(total_cnt)