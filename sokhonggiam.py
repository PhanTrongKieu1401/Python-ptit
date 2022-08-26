import math
from re import S
test=int(input())
for i in range(test):
    s=input()
    kt=True
    for i in range(1,len(s)):
        if s[i-1]>s[i]:
            kt=False
            break
    if kt==False:
        print("NO")
    else:
        print("YES")
