s=input()
kq=""
dem=0
for i in range(1,len(s)):
    if dem==3:
        kq=","+kq
        dem=0
    kq=s[-i]+kq
    dem+=1
if dem==3:
    kq=s[0]+","+kq
else:
    kq=s[0]+kq
print(kq)