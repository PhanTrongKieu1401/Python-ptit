from decimal import Decimal
import math

class Point:
    def __init__(self,tung,hoanh):
        self.tung=tung
        self.hoanh=hoanh
    
    def distance(self,a):
        ans= math.sqrt(math.pow(self.tung-a.tung,2)+math.pow(self.hoanh-a.hoanh,2))
        return ans

    def peremiter(self,a,b):
        c1=self.distance(a)
        c2=self.distance(b)
        c3=a.distance(b)
        if c1+c2>c3 and c1+c3>c2 and c2+c3>c1:
            return "{:.3f}".format(c1+c2+c3)
        else: return -1

if __name__=="__main__":
    t=int(input())
    while t>0:
        arr=input().split()
        p1=Point(Decimal(arr[0]),Decimal(arr[1]))
        p2=Point(Decimal(arr[2]),Decimal(arr[3]))
        p3=Point(Decimal(arr[4]),Decimal(arr[5]))
        ans=p1.peremiter(p2,p3)
        if ans==-1:
            print("INVALID")
        else:
            print(ans)
        t-=1
