x=eval(input('enter a temperature:'))
if x<-273.15:
    print('temperature is invalid because it is below absolute zero')
elif x==-273.15:
    print('temperature is absolute zero')
elif 0>x>-273.15:
    print('temperature is below freezing point')
elif x==0:
    print('temperature is at freezing point')
elif 0<x<100:
    print('temperature is in the normal range')
elif x==100:
    print('temperature is at the boiling point')
elif x>100:
    print('temperature is above the boiling point')
