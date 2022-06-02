from random import choice
l=['canada','nigeria','benin','germany','france','ghana','brazil','sweden','russia','israel']
a=choice(l)
guess=';'
count=5
while guess!='':
    guess=input('guess a letter contained in a country name')
    if guess in a:
        b='-'*len(a)
         
