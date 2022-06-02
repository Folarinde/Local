from random import randint
x = randint(1,10)
y = eval(input('guess the number x:'))
if y==x:
    print('your guess is right')
else:
    print('try again')
