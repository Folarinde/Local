x=eval(input('enter a number'))
sq_rt=(1+(x/1))/2
for i in range(10):
    sq_rt=(sq_rt+(x/sq_rt))/2
print('the square root is:',sq_rt)
