import math
test=int(input())
for i in range(test):
    xauso1=input()
    xauso2=xauso1[::-1] #Lấy đảo
    so1=int(xauso1)
    so2=int(xauso2)
    if math.gcd(so1,so2)!=1:
        print("NO")
    else:
        print("YES")