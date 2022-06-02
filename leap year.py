x=eval(input('enter a year: '))
if x%4==0:
    if x%100==0:
        if x%400==0:
            print('this is a leap year')
        else:
            print('this is not a leap year')
    else:
        print('this is a leap year')
else:
    print('this is not a leap year')
