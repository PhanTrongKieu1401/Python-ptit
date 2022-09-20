test=int(input())
def kt(s):
    lock=True
    if len(s)<3:
        return False
    for i in range(0,len(s)-1):
        if s[i]==s[i+1]:
            return False
        if lock==True:
            if s[i]>s[i+1]:
                lock=False
        else:
            if s[i]<s[i+1]:
                return False
    return True
for i in range(test):
    s=input()
    if kt(s)==True:
        print("YES")
    else:
        print("NO")
