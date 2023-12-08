def f(arr):
    largest_value = float('-inf')
    smallest_value = float('inf')
    largest_row = 0
    smallest_row = 0
    largest_column = 0
    smallest_column = 0

    for y in range(len(arr)):
        for x in range(len(arr[y])):
            value = arr[y][x]
            if value < smallest_value:
                smallest_value = value
                smallest_column = x
                smallest_row = y
            if value > largest_value:
                largest_value = value
                largest_column = x
                largest_row = y

    result = largest_column, largest_row, smallest_column, smallest_row
    return result

arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]
print(f(arr))



arr = [[-38, 19], [5,40],[-7,11],[29,16]]
print(f(arr))

