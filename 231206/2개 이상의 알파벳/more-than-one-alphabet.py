def cal(A):
    dic = {}
    for i in range(len(A)-1):
        if A[i] in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    if len(dic) > 3:
        print(len(dic))
        return print("Yes")
    else:
        return print("No")
    
    


A = input()
cal(A)