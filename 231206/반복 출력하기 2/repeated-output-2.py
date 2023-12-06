def out(n):
    if n == 0:
        return
    out(n-1)
    print("HelloWorld")


n = int(input())
out(n)