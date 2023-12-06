arr = [[True,False],[True,True],[False,False]]

for row in arr:
    for x in range(0,len(row)):
        if row[x] == True:
            row[x] = False
        else:
            row[x] = True

print(arr)