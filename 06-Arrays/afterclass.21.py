arr = [15, 8, 31, 47, 2, 19]
arr2 = []
for x in range(1, (len(arr)+1)):
    arr2.append(arr[-x])
print(arr2)