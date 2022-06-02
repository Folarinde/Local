from math import log
n=eval(input('enter a value n:'))
s = 0
for i in range(1,n+1):
    s = s + 1/i
x=s-log(n)
print(x)
