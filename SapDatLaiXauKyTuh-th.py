t=int(input())
for i in range(t):
    print("Test ",i+1,": ",sep="",end="")
    s1=sorted(input())
    s2=sorted(input())
    if s1==s2:
        print("YES")
    else:
        print("NO")