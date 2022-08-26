test=int(input())
for i in range(test):
    n,x,m=[float(x) for x in input().split()]
    x=1+x/100
    nam=0
    while n<m:
        n=n*x
        nam=nam+1
    print(nam)