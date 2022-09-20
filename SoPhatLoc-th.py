t=int(input())
for i in range(t):
    xau=input()
    if len(xau)<2:
        print("NO")
    else:
        if xau[-1]=='6' and xau[-2]=='8':
            print("YES")
        else: print("NO")