t=int(input())
for i in range(t):
    xau=input()
    ans=""
    dem=1
    for j in range(1,len(xau)):
        if xau[j]==xau[j-1]:
            dem+=1
        else:
            ans=ans+str(dem)+xau[j-1]
            dem=1
    ans=ans+str(dem)+xau[-1]
    print(ans)