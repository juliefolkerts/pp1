def f(array2D):
    result = 0
    for i in range(0,len(array2D)):
        sum_column = 0
        for j in range(0,len(array2D[0])):
            sum_column += array2D[i][j]
        if sum_column != sum(array2D[i]):
            result += 1
    if result > 0:
        a = False
    else:
        a = True
    return a

if __name__ == '__main__':
    array2D = [[3,7,2],[4,2,5],[5,2,1]]
    print(f(array2D))
    arrayD = [[3,7,2],[4,2,5],[9,2,1]]
    print(f(arrayD))
