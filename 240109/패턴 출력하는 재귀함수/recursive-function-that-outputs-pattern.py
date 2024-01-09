n = int(input())

if n > 369:
    for i in range(369, n+1, 1):
        if i % 2 != 0:
            print(i, end=' ')
elif n < 369:
    for k in range(n, 370, 1):
        if k % 2 != 0:
            print(k, end=' ')