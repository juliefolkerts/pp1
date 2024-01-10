def f(arr):
    result = 0
    for nr in arr:
        result ^= nr
    return result

if __name__ == '__main__':
    print(f([6,6,6,6,4,4,5,2,2,2,2,2,2]))