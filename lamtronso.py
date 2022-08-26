t=int(input())
for i in range(t):
    s=input()
    ok=1
    ans=""
    for i in range(1,len(s)):
        ans+='0'
        if ok==1:
            if int(s[-i])>4:
                ok=0
            else:
                ok=1
        else:
            if int(s[-i])>3:
                ok=0
            else:
                ok=1
    if ok==0:
        if s[0]=='9':
            ans+='0'
            ans='1'+ans
        else:
            ans=chr(ord(s[0])+1)+ans
    else:
        ans=s[0]+ans
    print(ans)