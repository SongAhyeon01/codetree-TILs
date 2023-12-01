lenA, lenB = map(int, input().split())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

flag = False
for i in listA:
    for k in listB:
        if i == k:
            flag = True
            break
    if flag:
        break

if flag == True:
    print('Yes')
else:
    print("No")