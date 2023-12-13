def f(arr):
    top = 41*'-'
    bottom = 41*'-'
    result = '|'
    for i in range(0, 8):
        if arr[i] < 10:
            result += f'   {str(arr[i])}|'
        elif 9<arr[i]<100:
            result += f'  {str(arr[i])}|'
        else:
            result += f' {str(arr[i])}|'
    return result
top = 41*'-'
bottom = 41*'-'

import random
x = 0
arr = []
for x in range(0,8):
    numbs = (random.randint(1,999))
    arr.append(numbs)
    x += 1

print(top)
print(f(arr))
print(bottom)
