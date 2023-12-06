def cal(a, b):
    result = []
    if a>b:
        big = a+25
        small = b*2
        result.append(big)
        result.append(small)
    else:
        big = b+25
        small = a*2
        result.append(small)
        result.append(big)
    return result


a, b = map(int, input().split())
print(*cal(a, b))