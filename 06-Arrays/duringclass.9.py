thisarray = [2, 3, 7, 5, 4]
#a.	the array
#b.	number of elements
#c.	first value
#d.	second value
#e.	last value
#f.	last but one value (do not use negative index values)
#g.	sum of the first and last value
#h.	middle value
#i.	all array values separated by a single space (use a loop statement)
#j.	first half of the array values, separated by a single space (use a loop statement)

#a
print(f'a= {thisarray}')
#b
print(f'b= {len(thisarray)}')
#c
print(f'c= {thisarray[0]}')
#d
print(f'd= {thisarray[1]}')
#e
print(f'e= {thisarray[-1]}')
#f
print(f'f= {thisarray[3]}')
#g
a = int(thisarray[0])
b = int(thisarray[-1])
c = int(a + b)
print(f'g= {c}')
#h
print(f'h= {thisarray[2]}')
#i
thisarray = [2, 3, 7, 5, 4]
def f():
    listarray = []
    for x in range(0, len(thisarray)):
        listarray.append(str(thisarray[x]))
    result = ' '.join(listarray)
    return result
print(f'i= {f()}')

#listarray = list(thisarray)
#result = ' '.join(listarray)
#print(result)
#j
thisarray = [2, 3, 7, 5, 4]
def j():
    emptylist = []
    for x in range(0, 3):
        emptylist.append(str(thisarray[x]))
    result = ' '.join(emptylist)
    return result
print(f'j= {j()}')
