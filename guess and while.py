from random import randint

secret_num = randint(1,100)
num_guesses = 0
guess = 0
x='guesses'

while guess != secret_num and num_guesses <= 4:
    guess = eval(input('Enter your guess (1-100): '))
    num_guesses = num_guesses + 1
    y=5-num_guesses
    if y==1:
        x=x[:-2]
    else:
        x=x[:]
    if guess < secret_num:
        print('HIGHER.',y,x,'left.\n')
    elif guess > secret_num:
        print('LOWER.',y,x,'left.\n')
    else:
        print('You got it!')
        
if num_guesses==5 and guess != secret_num:
    print('You lose. The correct number is', secret_num)
