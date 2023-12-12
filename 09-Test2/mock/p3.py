def f(array2D):
    sum_rows = []
    sum_columns = [] #verti
    for i in range(0,len(array2D)):
        sum_rows.append(sum(array2D[i]))
        x = sum(row[i] for row in array2D)
        sum_columns.append(x)
    if sum_rows == sum_columns:
        result = True
    else:
        result = False
    return result

print(f([[3,7,2],[4,2,5],[5,2,1]]))
print(f([[3,7,2],[4,2,5],[9,2,1]]))
        
    