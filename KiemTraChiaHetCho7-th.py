t=int(input())
for i in range(t):
    n=int(input())
    if n%7==0:
        print(n)
    else:
        while n%7!=0:
            val=str(n)
            val=int(val[::-1])
            n=n+val
        print(n)