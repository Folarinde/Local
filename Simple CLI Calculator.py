print('''This is a simple CLI calculator that performs addition(+),
subtraction(-), division(/), multiplication(*) and modulus(%) operations.''')

num1=input('enter first number:')
operator=input('Enter operation:')
num2=input('enter second number:')

try:
    num1=float(num1)
    num2=float(num2)

    if operator=='+':
        print('=',num1+num2)
    elif operator=='-':
        print('=',num1-num2)
    elif operator=='/':
        if num2==0:
            print('Division by 0 cannot be completed')
        else:
            print('=',num1/num2)
    elif operator=='*':
        print('=',num1*num2)
    elif operator=='%':
        if num2==0:
            print('Modulo by 0 cannot be completed')
        else:
            print('=',num1%num2)
    else:
        print('Invalid operation. Try again!')

except:
    print('One of the input is not a number. Please check and enter a number')
    