from random import randint
l=[]
for i in range(0,100):
    x=randint(0,1)
    l.append(x)
print(l)
a=0
b=0
for j in l:
    if j==0:
        a+=1
    else:
        if a>b:
            b=a
        a=0
print(b)
