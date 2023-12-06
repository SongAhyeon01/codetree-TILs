def cal(A):
    dic = {}
    for i in range(len(A)-1):
        if A[i] in dic:
            dic[A[i]] += 1
        else:
            dic[A[i]] = 1
    if len(dic) > 3:
        return print("Yes")
    else:
        return print("No")
    
    


A = input()
cal(A)