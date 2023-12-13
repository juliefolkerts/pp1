def f(arr):
    count = {}
    for value in arr:
        if value in count:
            count[value] += 1
        else:
            count[value] = 1
    unique_count = 0
    for key in count:
        if count[key] == 1:
            unique_count += 1
    return unique_count

if __name__ == '__main__':
    arr1 = [11,22,33,11]
    arr2 = [11,22,11,11,22,35,27,11,22,14]
    print(f(arr1))
    print(f(arr2))