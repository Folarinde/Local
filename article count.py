count=0
x=input('enter a text: ')
X=x.split()
articles=['a','an','the']
count=sum(1 for c in X if c in articles)

print('there are:',count, 'articles in the text')
