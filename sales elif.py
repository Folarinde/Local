x=eval(input('How many items are you buying?'))
if x<10:
    print('Totatal cost is: $',12*x)
elif 10<=x<=99:
    print('total cost is: $',10*x)
else:
    print('Total cost is: $',7*x)

