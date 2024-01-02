def fun(n):
    if n<3:
        return print(n, end=' ')
    fun(n//3)
    print(n, end=' ')

n = int(input())
fun(n)