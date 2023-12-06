def pal(A):
    B = ''
    for i in range(len(A)-1, -1, -1):
        B += A[i]
    if  A == B:
        return print("Yes")
    else:
        return print("No")


string = input()
pal(string)