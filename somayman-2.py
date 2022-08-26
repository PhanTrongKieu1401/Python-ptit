test=int(input())
for i in range(test):
    n=input()
    kt=1
    for i in range(len(n)):
        if n[i]!='4' and n[i]!='7':
            kt=0
            break
    if kt==1:
        print("YES")
    else:
        print("NO")