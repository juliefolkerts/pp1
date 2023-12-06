arr1 = [4,36,12,28,9,44,5] 
arr2 = [5,1,36]
result = []
for index1 in range(0,len(arr1)):
    if arr1[index1] in arr2:
        result = result
    else:
        result.append(arr1[index1])

print(result)