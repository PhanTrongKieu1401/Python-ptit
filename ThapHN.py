def Try(n,a,b,c):
    if n==1:
        print(a,"->",c)
    else:
        Try(n-1,a,c,b)
        Try(1,a,b,c)
        Try(n-1,b,a,c)

a='A'
b='B'
c='C'
n=int(input())
Try(n,a,b,c)
