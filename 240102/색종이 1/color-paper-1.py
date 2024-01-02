n = int(input())

li = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            li[i][j] += 1


result = 0
for k in range(100):
    for s in range(100):
        if li[k][s] >= 1:
            result += 1


print(result)