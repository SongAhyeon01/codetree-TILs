def cal(A):
    cnt = 0
    for i in range(len(A)-1):
        st = A[i]
        for k in range(i, len(A)-1):
            if st != A[k]:
                cnt += 1
            if cnt < 3:
                return print("Yes")
        if cnt < 3:
            return print("Yes")
    return print("No")
    
    


A = input()
cal(A)