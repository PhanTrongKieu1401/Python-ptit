t=int(input())
for i in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    minf=min(a[0],a[1],a[2])
    mint=max(a[0],a[1],a[2])   
    for j in range(0,3):
        if a[j]!=minf and a[j]!=mint:
            mins=a[j]
    for j in range(3,len(a)):
        x=a[j]
        if x<mint:
            if x<mins:
                if x<minf:
                    mint=mins
                    mins=minf
                    minf=x
                else:
                    mint=mins
                    mins=x
            else:
                mint=x
    print(minf+mins+mint)