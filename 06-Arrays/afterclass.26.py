arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
count = 0
answer = ''
for index in range(0, len(arr)):
    if len(arr[index]) > count:
        count = len(arr[index])
        answer = arr[index]

print(answer)