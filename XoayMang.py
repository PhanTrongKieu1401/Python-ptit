t=int(input())
for i in range(t):
    n,d=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    for j in range(d,len(a)):
        print(a[j],end=" ")
    for j in range(0,d):
        print(a[j],end=" ")
    print()