l=[1,3,4,6,8,9]
y=[]
z=[]
count=0
flag=0
from random import randint,choice,sample
for i in range(10):
    y.append(randint(1,10))
for j in range(100):
    draw=sample(y,6)
    print(draw)
print('It takes an average of',flag,'drawings before users numbers are drawn')
