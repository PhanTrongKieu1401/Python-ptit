t=int(input())
for i in range(t):
    p,q=[x for x in input().split()]
    a=input().strip()
    if(a.count(' ')) : a,b=a.split()
    else: b=input()
    m=min(p,q)
    n=max(p,q)
    print(int(a.replace(n,m))+int(b.replace(n,m)),end=" ")
    print(int(a.replace(m,n))+int(b.replace(m,n)))
