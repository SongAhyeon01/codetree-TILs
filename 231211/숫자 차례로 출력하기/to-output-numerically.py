def rec1(n):
    if n == 0:
        return
    
    rec1(n-1)
    print(n, end=' ')

def rec2(n):
    if n == 0:
        return
    
    print(n, end=' ')
    rec2(n-1)


n = int(input())
rec1(n)
print()
rec2(n)