t=int(input())
for i in range(t):
    n,m=[int(x) for x in input().split()]
    a,b=[[0]*m]*n,[]
    for x in range(n):
        a[x]=[int(y) for y in input().split()]
    for p in range(m):
        x=[]
        for q in range(n):
            x.append(a[q][p])
        b.append(x)
    for p in range(n):
        for q in range(n):
            s=0
            for z in range(m):
                s+=a[p][z]*b[z][q]
            print(s,end=' ')
        print()
