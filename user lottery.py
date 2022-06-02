l=[1,3,4,6,8,9]
y=[]
count=0
flag=0
from random import randint,sample
for j in range(1000000):
    for i in range(10):
        y.append(randint(1,10))
    draw=sample(y,6)
    if draw!=l:
        flag+=1
    else:
        count+=1
        if count==1:
            print('It takes an average of',flag,'drawings before users numbers are drawn')
