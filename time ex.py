x=eval(input('enter hour between 1 and 12 '))
y=eval(input('am (1) or pm (2)? '))
z=eval(input('how many hours ahead? '))
k=x+z
l=k//12
if x!=12 and y==1:
    if k%12==0:
        if l%2==0:
            print('New hour is : 12 am')
        else:
            print('New hour is : 12 pm')
    elif k%12!=0:
        if l%2==0:
            print('New hour is :',k%12,'am')
        else:
            print('New hour is :',k%12,'pm')
elif x!=12 and y==2:
    if k%12==0:
        if l%2==0:
            print('New hour is : 12 pm')
        else:
            print('New hour is : 12 am')
    elif k%12!=0:
        if l%2==0:
            print('New hour is :',k%12,'pm')
        else:
            print('New hour is :',k%12,'am')
elif x==12 and y==1:
    if k%12==0:
        if l%2==0:
            print('New hour is : 12 pm')
        else:
            print('New hour is : 12 am')
    elif k%12!=0:
        if l%2==0:
            print('New hour is :',k%12,'pm')
        else:
            print('New hour is :',k%12,'am')
if x==12 and y==2:
    if k%12==0:
        if l%2==0:
            print('New hour is : 12 am')
        else:
            print('New hour is : 12 pm')
    elif k%12!=0:
        if l%2==0:
            print('New hour is :',k%12,'am')
        else:
            print('New hour is :',k%12,'pm')
