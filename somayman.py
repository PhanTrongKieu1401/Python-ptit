n=input()
dem=0
for i in range(len(n)):
    if n[i]=='4' or n[i]=='7':
        dem=dem+1
if dem==4 or dem==7:
    print("YES")
else:
    print("NO")