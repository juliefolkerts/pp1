def f(arr2D):
    # Check if the 2D array has at least two columns
    if any(len(row) < 2 for row in arr2D):
        return False
    
    column_sums = [sum(map(lambda row: row[i], arr2D)) for i in range(len(arr2D[0]))]

    return any(column_sums.count(sum_val) >= 2 for sum_val in column_sums)

if __name__=='__main__':
    print(f([[3, 4, 2], [5, 1, 6]]))   # True
    print(f([[3, 4, 2], [5, 1, 7]]))   # False
    print(f([[3, 4], [5, 1], [4, 7]]))  # True
    print(f([[3, 4], [5, 9], [4, 7]])) #false