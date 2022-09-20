test=int(input())
for i in range(test):
    n=int(input())
    if n%7!=0:
        while n%7!=0:
            m=str(n)
            n=n+int(m[::-1])
    print(n)