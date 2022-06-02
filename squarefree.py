flag=0
x=eval(input('enter a number:'))
for i in range(2,x):
    if x%(i**2)==0:
        flag=flag+1
if flag>=1:
    print(x,'is not squarefree')
else:
    print(x,'is squarefree')
