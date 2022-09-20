from operator import truediv


import math
test=int(input())
for i in range(test):
    n=input()
    kt=True
    tong=int(n[0])-int('0')
    for i in range(1,len(n)):
        if abs(int(n[i])-int(n[i-1]))!=2:
            kt=False
            break
        else:
            tong=tong+int(n[i])-int('0')
    if tong%10!=0:
        kt=False
    if kt==True:
        print("YES")
    else:
        print("NO")