def check(xau):
    n=0
    for i in range(len(xau)):
        n+=ord(xau[i])-ord('0')
    return str(n)
    
n=input()
dem=0
while(len(n)>1):
    n=check(n)
    dem+=1
print(dem)