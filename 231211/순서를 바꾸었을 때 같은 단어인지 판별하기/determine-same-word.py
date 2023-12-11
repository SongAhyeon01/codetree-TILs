a = input()
b = input()

aa = sorted(a)
bb = sorted(b)

aa = ''.join(aa)
bb = ''.join(bb)

if aa == bb:
    print("Yes")
else:
    print("No")