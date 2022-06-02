s=input('enter a string')
print(len(s))
print(s*10 ,end='')
print(s[0])
print(s[:3],s[-3:],s[::-1])
if len(s)>7:
    print(s[6])
else:
    print('string is not long enough')
print(s[1:-1],s.upper(),s.replace('a','e'))
for c in s:
    print(s.replace(c,' '))
