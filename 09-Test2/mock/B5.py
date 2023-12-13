def f(arr2D):
    count = 0
    for arr in arr2D:
        if int(arr[1]) == (int(arr[0])**2):
            count += 1
        else:
            count = count
    return count

if __name__ == '__main__':
    arr1 = [[4,16], [3,9], [-3,9]]
    arr2 = [[4,15], [3,9], [-3,-9]]
    print(f(arr1))
    print(f(arr2))