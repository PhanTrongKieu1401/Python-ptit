
#a+bi (a+c)+(b+d)i  a(a+c)-b*(b+d)+(a*(b+d)+b*(a+c))i
#(a+c)*(a+c)-(b+d)*(b+d)   2*(a+c)*(b+d)
#a+bi   (a+c)+(b+d)i
#a*(b+d)+b*(a+c)
import math


if __name__=="__main__":
    t=int(input())
    for i in range(t):
        a,b,c,d=[int(x) for x in input().split()]
        
        print(a*(a+c)-b*(b+d),end=' ')
        if a*(b+d)+b*(a+c)<0:
            print("-",abs(a*(b+d)+b*(a+c)),end='i, ')
        else:
            print("+",a*(b+d)+b*(a+c),end='i, ')
        
        print((a+c)*(a+c)-(b+d)*(b+d),end=' ')
        if 2*(a+c)*(b+d)<0:
            print("-",(-2)*(a+c)*(b+d),end='i')
            print()
        else:
            print("+",2*(a+c)*(b+d),end='i')
            print()
