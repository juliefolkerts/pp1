arr1 = [3,7,1,0,4]
print(f'a {arr1}')
arr2 = [[2,3],[7,1],[0,4]]
print(f'b. {arr2}')
arr3 = [7 for i in range(5)]
print(f'c. {arr3}')
arr4 = [i for i in range(1,10)]
print(f'd. {arr4}')
arr5 = [i*2 for i in range(1,10)]
print(f'e. {arr5}')
import random
arr6 = [random.randint(1,20) for i in range(10)]
print(f'f. {arr6}')
arr7 = [[] for i in range(5)]
print(f'g. {arr7}')
arr8 = [[1 for i in range(2)] for j in range(4)]
print(f'h. {arr8}')
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
print(f'i. {arr9}')
#an array with values: 4,0,3
arr10 = [4, 0, 3]
print(f'i. {arr10}')
#15-element array filled with zeros
arr11 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(f'j. {arr11}')
#an array with integer values in the range of <1,30>
arr12 = []
for x in range(0,31):
    arr12.append(x)
print(f'k. {arr12}')
#20-element array filled with 0 or 1 randomly
import numpy as np
arr13 = np.random.randint(2, size = 20)
print(f'l. {arr13}')
#two dimensional array with five rows and two columns filled with False
rows = 5
columns = 2
arr14 = [[False]* columns for x in range(0,rows)]
print(f'm. {arr14}')