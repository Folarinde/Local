for i in range(10):
    s=input('enter any string:')
    l=input('enter any letter:')
    
    if l not in s:
        print('Done. String does not contain letter')
        break
    print(s.index(l),s)
