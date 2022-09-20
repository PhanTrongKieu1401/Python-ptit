import math
n,k=(int(x) for x in input().split())
dau=10**(k-1)
cuoi=10**k
dem=1
for i in range(dau,cuoi):
    if math.gcd(n,i)==1:
        print(i,end=" ")
        if dem%10==0:
            print()
        dem+=1