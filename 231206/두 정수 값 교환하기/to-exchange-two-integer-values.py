def switch(n, m):
    n, m = m, n
    return n, m

n, m = map(int, input().split())
print(*switch(n, m))