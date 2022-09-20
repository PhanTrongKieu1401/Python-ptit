def check(n):
    xauxuoi=str(n)
    xaunguoc=xauxuoi[::-1]
    if xauxuoi!=xaunguoc:
        return 0
    if len(xauxuoi)%2!=0:
        return 0
    for i in range(len(xauxuoi)):
        if int(xauxuoi[i])%2!=0:
            return 0
    return 1
t=int(input())
for i in range(t):
    n=int(input())
    for i in range(22,n,2):
        if check(i)==1:
            print(i,end=" ")
    print()
