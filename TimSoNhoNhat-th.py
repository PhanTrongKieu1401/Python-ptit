t=int(input())
for i in range(t):
    xau=input()
    xau+='z'
    ans=10**19
    val=0
    for j in range(len(xau)):
        if xau[j].isalpha():
            if j!=0 and xau[j-1].isdigit():
                ans=min(ans,val)
                val=0
        else: val=val*10+int(xau[j])
    print(ans)