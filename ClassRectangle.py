class Rectangle:
    def __init__(self,long,wight,colo):
        self.long=long
        self.wight=wight
        self.colo=colo
    def check(self):
        if self.long<=0 or self.wight<=0: return 0
        return 1
    def perimeter(self):
        if self.check==0:
            print("INVALID")
        else:
            return 2*(self.long+self.wight)
    def area(self):
        if self.check==1:
            return self.long*self.wight
    def color(self):
        if self.check==1:
            return self.colo[0:1:].upper()+self.colo[1::].lower()

if __name__=='__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(),r.area(),r.color()))