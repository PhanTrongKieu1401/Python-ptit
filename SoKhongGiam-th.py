t=int(input())
for i in range(t):
    xau=input()
    check=True
    for j in range(1,len(xau)):
        if xau[j]<xau[j-1]:
            check=False
            break
    if check==True:
        print("YES")
    else: print("NO")