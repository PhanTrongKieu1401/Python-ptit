s1=input()
s2=input()
p=int(input())
ans=s1[0:(p-1)]
print(ans,end='')
print(s2,end='')
ans=s1[(p-1):]
print(ans)