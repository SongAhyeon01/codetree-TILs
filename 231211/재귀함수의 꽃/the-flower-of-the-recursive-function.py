def rec(n):
    if n == 0:
        return
    
    print(n, end=' ')
    rec(n-1)
    print(n, end=' ')


n = int(input())
rec(n)