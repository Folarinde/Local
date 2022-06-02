m=[]
l=[1,25,36,25,8,9,36,8,9,9,9,0,94,52,94,94]
for i in range(len(l)):
    if l[i] not in m:
        m.append(l[i])
print(m)
