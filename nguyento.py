import math
from operator import truediv
def nt(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True          
t=int(input())
for i in range(t):
    n=int(input())
    dem=0
    for j in range(1,n):
        if math.gcd(j,n)==1:
            dem=dem+1
    if nt(dem)==False:
        print("NO")
    else: print("YES")