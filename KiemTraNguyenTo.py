import math

def ktnt(x):
    if x<2:
        return False
    for j in range(2,math.trunc(math.sqrt(tong))+1):
        if tong%j==0:
            return False
    return True

t=int(input())
for i in range(t):
    n=input()
    tong=0
    for j in range(1,5):
        tong=tong*10+int(n[-(5-j)])-int('0')
    if ktnt(tong)==True:
        print("YES")
    else:
        print("NO")