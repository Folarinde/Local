from random import randint
for i in range(1,11):
    x=randint(1,10)
    y=randint(1,10)
    z=x*y
    print(x,'X',y,'=')
    Q1=eval(input('the answer is: '))
    if Q1==z:
        print('correct')
    else:
        print('wrong! the answer is: ',z)
