import math


t=int(input())
for i in range(t):
    n,x,m=[float(z) for z in input().split()]
    x=1+x/100
    j=0
    ans=n*math.pow(x,j)
    while ans<m:
        j+=1
        ans=n*math.pow(x,j)
    print(j)