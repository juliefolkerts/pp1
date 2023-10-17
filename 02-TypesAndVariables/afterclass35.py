import math
circumference = int(input('Enter circumference of tree in cm: \n'))
diameter = (circumference / (math.pi))
if (diameter >= 50) :
    print('Tree can be cut down: True')
else:
    print('Tree can be cut down: False')