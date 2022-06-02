password='Stew789$'
b=0
w=eval(input('enter password: '))
while w!=password:
    w=eval(input('invalid password. try again: '))
    b=b+1
    if b==4:
        print('youre kicked out')
        break
else:
    print('Youre logged in')
