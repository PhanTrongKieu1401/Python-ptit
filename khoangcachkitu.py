import math
test=int(input())
for i in range(test):
    xauxuoi=input()
    xaudao=xauxuoi[::-1]
    kt=True
    for j in range(len(xauxuoi)-1):
        if abs(ord(xauxuoi[j])-ord(xauxuoi[j+1]))!=abs(ord(xaudao[j])-ord(xaudao[j+1])):
            kt=False
            break
    if kt==True:
        print("YES")
    else:
        print("NO")