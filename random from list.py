from random import choice

l=['seven','level','bang','figurine','discuss','throne','force','ballad','blast','barb']
z=[]
y=[]
flag=0

for c in l:
    for i in c:
        b=c.count(i)
        if b>1:
            flag+=1
            if flag==1:
                z.append(c)
    flag=0

for c in l:
    if c not in z:
        y.append(c)

print(choice(y))
