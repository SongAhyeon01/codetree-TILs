def rec(n):
    if n<=2:
        return n
    
    if n%2 != 0:
        return rec(n-2)+n
    else:
        return rec(n-2)+n
    
n = int(input())
print(rec(n))