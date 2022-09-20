test=int(input())
for i in range(test):
    s=input()
    if len(s)<2:
        print("NO")
    else:
        if s[-1]=='6' and s[-2]=='8':
            print("YES")
        else: print("NO")