#a.	the array
#b.	size of the array (number of rows and columns)
#c.	value 5 from the array
#d.	value 3 from the array
#e.	second row of the array as below:
#9 0 3


thisarray = [[2,5,4],[9,0,3]]

row2 = thisarray[1]
result = ' '.join(map(str, row2))
print(f'e. {result}')


