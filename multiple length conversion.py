x=[1,2,3,4,5,6,7]
p=['inches','yards','miles','millimetres','centimetres','metres','kilometres']
y=[12,0.3,0.0001893,304.8,30.48,0.3048,0.0003048]
z=eval(input('enter length in feet; '))
print("""1 for inches, 2 for yards, 3 for miles, 4 for millimetres,
5 for centimetres, 6 for metres, 7 for kilometres""")
q=eval(input('enter new unit code: '))
if q in x:
    print('in',p[x.index(q)], 'that is: ',(y[x.index(q)]*z),p[x.index(q)])
else:
    print('wrong unit code entered')
