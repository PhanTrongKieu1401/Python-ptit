t=int(input())
for i in range(0,t):
    n=int(input())
    a=sorted([int(x) for x in input().split()]) #nhap xong sap xep
    dem=0
    for j in range(0,n-2):
        left=j+1
        right=len(a)-1
        #x=a[j]
        while left<right:
            if a[j]+a[left]+a[right]==0:
                dem+=1
                left+=1
            elif a[j]+a[left]+a[right]<0:
                left+=1
            else: right-=1
    print(dem)
