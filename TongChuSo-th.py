def tong(xau):
    n=0
    for i in range(len(xau)):
        n+=ord(xau[i])-ord('0')
    return str(n)

n=input()
dem=0
while(len(n)>1):
    n=tong(n)
    dem+=1
print(dem)
