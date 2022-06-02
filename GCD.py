l=eval(input('enter larger number for gcd: '))
s=eval(input('enter smaller number for gcd: '))
x=l%s
while x!=0:
    l,s=s,x
    x=l%s
print(s,'is the GCD.') 