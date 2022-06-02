s=0
score=0
count=0
count2=0
while score>=0:
    score=eval(input('enter score: '))
    count+=1
    s=s+score
    if score>=90:
        count2+=1
print('average is:',(s-score)/(count-1),'and there are',count2,'As')
