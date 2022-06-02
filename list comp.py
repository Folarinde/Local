l=[[1,2,3,4,5] for i in range(5)]
print(l)
for r in range(5):
    for c in range(5):
        print(l[r][c],end='')
    print()
print([l[i][2] for i in range(5)])
print([j for i in l for j in i])
