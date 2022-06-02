from random import randint,sample
l=[]
for i in range(1,49):
    l.append(randint(1,48))
print(l)
draw=sample(l,6)
print(draw)
