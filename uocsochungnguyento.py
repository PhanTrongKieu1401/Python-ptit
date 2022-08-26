from math import gcd
import math
def ktnt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
test=int(input())
for i in range(test):
    x,y=[int(z) for z in input().split()]
    n=math.gcd(x,y)
    tong=0
    while n>0:
        tong=tong+n%10
        n=int(n/10)
    if ktnt(tong)==True:
        print("YES")
    else:
        print("NO")