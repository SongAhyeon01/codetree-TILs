a = list(map(int, input().split()))

start = min(a)
end = max(a)
mid = 0

for i in a:
    if (i != start) and (i != end):
        mid = i


for front in range(start, end+1):
    if front != mid:
        for back in range(1, 10):
            print(front, "*", back, "=", front*back)