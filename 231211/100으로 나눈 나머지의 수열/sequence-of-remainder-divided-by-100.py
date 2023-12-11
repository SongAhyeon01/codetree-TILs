def rec(n):
    if n==1:
        return 2
    if n==2:
        return 4

    return rec(n-1)*rec(n-2)%100


n = int(input())
print(rec(n))