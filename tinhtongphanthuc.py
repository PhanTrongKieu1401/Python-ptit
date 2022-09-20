test=int(input())
for i in range(test):
    n=int(input())
    tong=float(0)
    if n%2==0:
        for j in range(2,n+1,2):
            tong=float(tong+1/j)
    else:
        for j in range(1,n+1,2):
            tong=float(tong+1/j)
    print('%.6f' % tong)