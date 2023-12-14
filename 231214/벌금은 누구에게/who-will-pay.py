n, m, k = map(int, input().split())

s_list = [0 for i in range(n+1)]

for i in range(m):
    s = int(input())
    s_list[s] += 1

    if s_list[s] >= k:
        print(s)
        break
else:
    print(-1)