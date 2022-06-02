from random import randint
score=0
for i in range(5):
    x=randint(1,10)
    y=eval(input('guess a number'))
    if y==x:
        score=score+10
        print('correct')
    else:
        score=score-1
        print('wrong')
print('final score is ',score)