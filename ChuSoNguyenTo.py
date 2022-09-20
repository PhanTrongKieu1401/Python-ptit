import math

def check(n):
    for i in range(2,math.trunc(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

t=int(input())
for i in range(t):
    xau=input()
    if check(len(xau))==0:
        print("NO")
    else:
        dem=0
        for j in range(len(xau)):
            if xau[j]=='2' or xau[j]=='3' or xau[j]=='5' or xau[j]=='7':
                dem+=1
        if dem>len(xau)-dem:
            print("YES")
        else: print("NO")