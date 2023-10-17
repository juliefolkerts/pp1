x = 7
y = 34
print('Value of x is: 7') #why doesn't it work to put x in this?
print('Value of y is: 34') #same here?

temp = x
x = y
y = temp

print('Value of x after swapping: {}'.format(x))
print('Value of y after swapping: {}'.format(y))