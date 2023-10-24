x = int(input('Enter x :'))
y = int(input('Enter y:'))
if x > 0 and y > 0:
    print(f'Point P({x, y}) is in the first quadrant of the coordinate system')
elif x < 0 and y > 0:
    print(f'Point P({x, y}) is in the second quadrant of the coordinate system')
elif x < 0 and y < 0:
    print(f'Point P({x, y}) is in the third quadrant of the coordinate system')
elif x > 0 and y < 0:
    print(f'Point P({x, y}) is in the fourth quadrant of the coordinate system')
elif x == 0:
    print(f'Point P({x, y}) is on the x acis')
elif y == 0:
    print(f'Point P{x, y} is on the y acis')
else:
    print('Point P(0,0) is the origin')
