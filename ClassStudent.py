class student:
    def __init__(self,name,date,score1,score2,score3) -> None:
        self.name=name
        self.date=date
        self.score1=score1
        self.score2=score2
        self.score3=score3
        self.tong=score1+score2+score3

    def output(self):
        print(self.name,self.date,"{:.1f}".format(self.tong))

if __name__=="__main__":
    a=student(input(),input(),float(input()),float(input()),float(input()))
    a.output()
