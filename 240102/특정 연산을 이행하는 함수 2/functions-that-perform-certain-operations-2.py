import math

a = list(map(float, input().split()))


for n in range(len(a)):
    if a[n] == max(a):
        a[n] = math.ceil(a[n])
    elif a[n] == min(a):
        a[n] = math.floor(a[n])
    else:
        a[n] = round(a[n])

print(max(a), end=' ')
print(min(a), end=' ')
for n in a:
    if n != max(a) and n != min(a):
        print(n)