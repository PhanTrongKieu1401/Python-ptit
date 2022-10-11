t=int(input())
for i in range(t):
    xau=input()
    ans=[]
    kq=0
    for j in range(len(xau)):
        if xau[j]>='0' and xau[j]<='9':
            kq+=ord(xau[j])-ord('0')
        else:
            ans.append(xau[j])
    ans.sort()
    for j in range(len(ans)):
        print(ans[j],end='')
    print(kq)