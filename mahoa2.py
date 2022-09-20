#hàm tách xâu
def tach(s):
    tong=0
    for i in range(len(s)):
        if s[i]==" ":
            return tong
        else:
            tong=tong*10+int(s[i])-int('0')
    return tong
#main
p="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
xau=input()
if xau!="0":
    while xau!="0":
        tong=tach(xau)
        kq=""
        for i in range(1,len(xau)):
            if xau[-i]==" ":
                break
            tg=p.find(xau[-i])
            tg=tg+tong
            tg=tg%28
            kq=kq+p[tg]
        print(kq)
        xau=input()

