s=input()
demhoa=0
demthuong=0
for i in range(len(s)):
    if s[i]>='A' and s[i]<='Z':
        demhoa=demhoa+1
    else:
        demthuong=demthuong+1
if demhoa<=demthuong:
    print(s.lower())
else:
    print(s.upper())