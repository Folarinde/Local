count1=0
count2=0
count3=0
for i in range(1,1001):
    x=i**2
    y=i**3
    z=i**5
    if x<=1000:
        count1=count1+1
    if y<=1000:
        count2=count2+1
    if z<=1000:
        count3=count3+1
print(1000-count1,'are not perfect squares')
print(1000-count2,'are not perfect cubes')
print(1000-count3,'are not perfect fifths')
