def rec(mul):
    if mul < 10:
        return mul
    
    return rec(mul//10) + mul%10
    


a, b, c = map(int, input().split())
mul = a*b*c
ans = rec(mul)
print(ans)