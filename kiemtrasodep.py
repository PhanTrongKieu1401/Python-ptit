test=int(input())
for i in range(test):
    setle={"a"}
    setchan={"a"}
    n=input()
    for j in range(0,len(n),2):
        setchan.add(n[j])
    for j in range(1,len(n),2):
        setle.add(n[j])
    if len(setle)==len(setchan) and len(setle)==2:
        print("YES")
    else:
        print("NO")