highest=0
lowest=100
s=0
flag=0
for i in range(10):
    x=eval(input('enter a score'))
    s=s+x
    if x>=highest:
        highest=x
    if x<=lowest:
        lowest=x
    if x>100:
        flag=flag+1
if flag>=1:
     print('a value over 100 has been entered')
print(highest,lowest,s/10)

