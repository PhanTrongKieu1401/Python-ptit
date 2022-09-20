test=int(input())
for j in range(test):
    s=input()
    i=0
    kq=""
    dem=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            dem+=1
        else:
            kq=kq+str(dem)+s[i-1]
            dem=1
    kq=kq+str(dem)+s[len(s)-1]
    print(kq)