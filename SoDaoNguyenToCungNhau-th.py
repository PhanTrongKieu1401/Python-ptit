import math


t=int(input())
for i in range(t):
    xau1=input()
    xau2=xau1[::-1]
    xau1=int(xau1)
    xau2=int(xau2)
    if math.gcd(xau1,xau2)==1:
        print("YES")
    else: print("NO")