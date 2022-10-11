import functools
from os import access
from re import sub
from unicodedata import name

class sv:
    def __init__(self,name,ac,submit) -> None:
        self.name=name
        self.ac=ac
        self.submit=submit
def cmp(self,a):
    if self.ac<a.ac:
        return 1
    elif self.ac==a.ac:
        if self.submit> a.submit:
            return 1
        elif self.submit==a.submit:
            if self.name>a.name:
                return 1
            else: return -1
        else: return -1
    else: return -1

n=int(input())
a=[]
for i in range(n):
    name=input()
    ac,submit=[int(x) for x in input().split()]
    a.append(sv(name,ac,submit))
a=sorted(a,key=functools.cmp_to_key(cmp))
for i in a:
    print(i.name,i.ac,i.submit)