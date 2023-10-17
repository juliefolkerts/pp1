x = 7
y = 34
print(f'Value of x is: {x}') 
print(f'Value of y is: {y}') 

temp = x
x = y
y = temp

print('Value of x after swapping: {}'.format(x))
print('Value of y after swapping: {}'.format(y))