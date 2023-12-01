def cal(n):
    list = []
    if n%2 != 0:
        for i in range(1, n+1, 2):
            list.append(i)
    else:
        for i in range(2, n+1, 2):
            list.append(i)
    return list


n = int(input())
print(*cal(n))