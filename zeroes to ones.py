from pprint import pprint
from random import choice,sample

z=[[0,0,0,0,0] for i in range(5)]
pprint(z)

for r in range(5):
    for c in range(5):
        print(z[r][c],end='')
    print()
