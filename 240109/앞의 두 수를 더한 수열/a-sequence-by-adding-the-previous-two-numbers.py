# 0 1 1 2 3 5

def fun(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else :
        return fun(n-1) + fun(n-2)


n = int(input())
result = fun(n+1)

print(result)