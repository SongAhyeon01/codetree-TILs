what_day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
day_of_mon = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


m1, d1, m2, d2 = map(int, input().split())

ss1 = 0
for i in range(m1):
    ss1 += day_of_mon[i]
ss1 += d1

ss2 = 0
for i in range(m2):
    ss2 += day_of_mon[i]
ss2 += d2

print(ss2-ss1)