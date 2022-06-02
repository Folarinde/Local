from random import shuffle
from string import punctuation
x=input('enter a sentence: ')
x=x.lower()
for i in punctuation:
    x=x.replace('.','')
X=x.split()
shuffle(X)
y=' '.join(X)
b=y[0]
b=b.upper()
y=b[:]+y[1:]
print(y,'.',sep='')
