from random import randint
a=100
while a>0:
    b=randint(0,1)
    guess=eval(input('Take a guess, heads or tails: 0 for tail and 1 for head, for coin tossed:'))
    if guess==b:
        a=a+9
        print('correct! you won $9. Total is $',a)
    else:
        a=a-10
        print('wrong! you lost $10. Total is $',a) 
    if a>=200:
        print('you win!')
        break
print('game over!')
