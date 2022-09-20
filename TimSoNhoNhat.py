t=int(input())
for i in range(t):
    s = input()
    s = s + 'z'
    ans = 10**19
    val = 0
    for j in range(len(s)):
        if s[j].isalpha():
            if j!=0 and s[j-1].isdigit(): ans=min(ans,val)
            val = 0
        else: val=val*10+int(s[j])
    print(ans)
     