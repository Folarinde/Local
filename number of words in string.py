flag=0
x=eval(input('how many email addresses? '))
for i in range(x):
    y=input('enter the email addresses: ')
    if '@prof.' in y:
        flag=flag+1
if flag>=1:
    print('some professor addresses were entered')
else:
    print('all addresses are student addresses')
