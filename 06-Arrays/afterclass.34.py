tup = (10,20,30,40,50)
newtup = []
for index in range(1,len(tup)+1):
    newtup.append(tup[-index])

print(tuple(newtup))