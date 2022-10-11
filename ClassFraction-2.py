import math
from re import A
from sre_constants import MAX_UNTIL


class fraction:
    def __init__(self,numerator,denominator) -> None:
        self.numerator=numerator
        self.denominator=denominator
    def multi(self,a):
        self.numerator=self.numerator*a.denominator+self.denominator*a.numerator
        self.denominator=self.denominator*a.denominator
    def compact(self):
        val=math.gcd(self.numerator,self.denominator)
        self.numerator=int(self.numerator/val)
        self.denominator=int(self.denominator/val)
    def out(self):
        print(self.numerator,"/",self.denominator,sep="")

if __name__=="__main__":
    numerator1,denominator1,numerator2,denominator2=[int(x) for x in input().split()]
    ps1=fraction(numerator1,denominator1)
    ps2=fraction(numerator2,denominator2)
    ps1.multi(ps2)
    ps1.compact()
    ps1.out()
    