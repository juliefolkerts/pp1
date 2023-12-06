arr = [12, 6, 4, 9, 10]

def star(n):
    stars = arr[n] * '*'
    return stars

max_width = len(str(max(arr)))

for n in range(0, len(arr)):
    spaces = ' ' * (max_width - len(str(arr[n])))
    print(f'{spaces}{arr[n]}:{star(n)}') 

#does it matter if the numbers don't match up?