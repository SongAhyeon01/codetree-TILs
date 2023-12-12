a, b, c = map(int, input().split())

if a <= 11 and b <= 11 and c <= 11:
    print(-1)


else:
    mm = a*24*60 + b*60 + c
    ss = 11*24*60 + 11*60 + 11
    print(mm-ss)