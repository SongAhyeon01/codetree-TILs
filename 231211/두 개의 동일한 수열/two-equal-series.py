n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]

aa = sorted(a)
bb = sorted(b)

if aa==bb:
    print("Yes")
else:
    print("No")