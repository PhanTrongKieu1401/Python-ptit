t=int(input())
a=[]
n=[int (x) for x in input().split()]
for i in n:
    if len(a)==0:
        a=a+[i]
    else:
        if (i+a[-1])%2==0:
            a.pop()
        else:
            a=a+[i]
print(len(a))