n = int(input())

list = [int(input()) for _ in range(n)]

cnt = 1
for i in range(len(list)):
    if i == 0 or list[i] != list[i-1]:
        cnt += 0
    else:
        cnt += 1
    

print(cnt)