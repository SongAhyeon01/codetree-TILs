def cal(A):
    dic = {}
    for i in range(len(A)-1):
        if A[i] in dic:
            print(A[i])
            dic[i] += 1
        else:
            dic[i] = 1
    if len(dic) > 3:
        return print("Yes")
    else:
        return print("No")
    
    


A = input()
cal(A)