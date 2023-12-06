arr = [15, 8, 31, 47, 2, 19]
total = 0
count = 0
while count < len(arr): 
    total += arr[count]
    count += 1

mean = total / count
print(mean)