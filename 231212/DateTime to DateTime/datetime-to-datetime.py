a, b, c = map(int, input().split())




mm = a*24*60 + b*60 + c
ss = 11*24*60 + 11*60 + 11

if mm<ss:
    print(-1)
else:
    print(mm-ss)