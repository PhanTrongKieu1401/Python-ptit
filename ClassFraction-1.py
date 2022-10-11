import math
from re import A
from sre_constants import MAX_UNTIL


class fraction:
    def __init__(self,numerator,denominator) -> None:
        self.numerator=numerator
        self.denominator=denominator
    def compact(self):
        val=math.gcd(self.numerator,self.denominator)
        self.numerator=int(self.numerator/val)
        self.denominator=int(self.denominator/val)
    def out(self):
        print(self.numerator,"/",self.denominator,sep="")

if __name__=="__main__":
    numerator,denominator=[int(x) for x in input().split()]
    ps=fraction(numerator,denominator)
    ps.compact()
    ps.out()