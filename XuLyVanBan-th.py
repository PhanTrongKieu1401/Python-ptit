import re
s=""
r='[\w\s,:]+'
while True:
    try: s+=input()
    except EOFError: break
s=re.findall(r,s)
for i in s:
    x=i.lower().split()
    x[0]=x[0].title()
    print(' '.join(x))