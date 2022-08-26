test=int(input())
for i in range(test):
    s=input()
    if s[0]==s[-2] and s[1]==s[-1]:
        print("YES")
    else:
        print("NO")