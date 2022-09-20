import math
test=int(input())
for i in range(test):
    n=int(input())
    kq="1" 
    d = 0
    while n%2==0 :
        n/=2
        d+=1
    if d:
        kq+=" * 2^"+str(d)
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0:
            d = 0
            while n%i==0:
                d+=1
                n/=i
            kq+=" * "+str(i)+"^"+str(d) 
    if n > 1 :
        kq += " * "+str(int(n))+"^1"
    print(kq)
             
    