n = int(input())

line = [0 for i in range(101)]
for _ in range(n):
    a, b = map(int, input().split())
    for j in range(a, b+1):
        line[j] += 1


print(max(line))