square = [[0]*2001 for _ in range(2001)]
v = ['a', 'b', 'm']

for w in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100

    for i in range(x1, x2):
        for j in range(y1, y2):
            square[i][j] = v[w]

cnt = 0
for k in range(2001):
    for m in range(2001):
        if square[k][m] == 'a' or square[k][m] == 'b':
            cnt += 1


print(cnt)