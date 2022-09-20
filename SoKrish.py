t=int(input())
a=[1]
for i in range(1,10):
    a.append(a[i-1]*i)
for i in range(t):
    n=int(input())
    x=n
    sum=0
    while(x>0):
        val=x%10
        sum+=a[val]
        x=int(x/10)
    if sum==n:
        print("Yes")
    else: print("No")