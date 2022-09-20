t=int(input())
for i in range(t):
    xau=input()
    check=True
    for i in range(len(xau)):
        if xau[i]!='0' and xau[i]!='1' and xau[i]!='2':
            check=False
            break
    if check==True:
        print("YES")
    else: print("NO")