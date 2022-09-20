test=int(input())
for i in range(test):
    s=input()
    kt=True
    for i in range(len(s)):
        if s[i]!='0' and s[i]!='1' and s[i]!='2':
            kt=False
    if kt==True:
        print("YES")
    else:
        print("NO")