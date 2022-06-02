x=eval(input('enter a temperature: '))
y=eval(input('What unit? enter 0 for celcius and any other number for fahrenheit'))
if y==0:
    print('temperature in fahrenheit is: ',(9/5)*x+32)
else:
    print('temperature in cslcius is:',(5/9)*(x-32))
