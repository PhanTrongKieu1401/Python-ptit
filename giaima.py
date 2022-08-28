t=int(input())
for i in range(t):
    s=input()
    kq=""
    for i in range(1,len(s),2):
        sl=int(s[i])
        for j in range(sl):
            kq=kq+s[i-1]
    print(kq)