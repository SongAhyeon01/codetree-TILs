S = list(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0
dir_num = 3

for k in S:
    if k == 'R':
        dir_num = (dir_num+1)%4
    elif k == 'L':
        dir_num = (dir_num+3)%4
    else:
        x, y = x+dx[dir_num], y+dy[dir_num]
print(x, y)