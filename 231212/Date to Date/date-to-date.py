m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

k1 = 0
for i in range(m1+1):
    k1 += num_of_days[i];
k1 += d1

k2 = 0
for i in range(m2+1):
    k2 += num_of_days[i];
k2 += d2


print(k2-k1)