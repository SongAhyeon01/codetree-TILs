n, m = map(int, input().split())

A = []
B = []


# A가 3번
# A[0] 부터 쭉 1씩 증가 or 감소하며 append
# A[0] ~ A[9] 는 R 이므로 0~9 를 append
# A[10] ~ A[12] 은 8~6 을 append (9-1 ~ 9-3)

loc = 0
A.append(0)
for i in range(1, n+1):
    d, t = map(str, input().split())
    t = int(t)

    if d == 'R':
        for k in range(t):
            loc += 1
            A.append(loc)
    else:
        for k in range(t):
            loc -= 1
            A.append(loc)

loc = 0
B.append(0)
for i in range(1, m+1):
    d, t = map(str, input().split())
    t = int(t)

    if d == 'R':
        for k in range(t):
            loc += 1
            B.append(loc)
    else:
        for k in range(t):
            loc -= 1
            B.append(loc)



for x in range(len(A)):
    if x != 0 and A[x] == B[x]:
        print(x)
        break
    else:
        print(-1)