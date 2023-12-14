n = int(input())


list = [int(input()) for _ in range(n)]

max_cnt = 1
cnt = 1
for i in range(n-1):
    if list[i] > 0:
        if list[i+1] > 0:
            cnt += 1
        else:
            cnt = 1
    else:
        if list[i+1] < 0:
            cnt += 1
        else:
            cnt = 1

    if cnt >= max_cnt:
        max_cnt = cnt


print(max_cnt)