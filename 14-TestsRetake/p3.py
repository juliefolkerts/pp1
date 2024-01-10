def f(arr2D):
    for x in arr2D:
        x[0],x[-1]=x[-1],x[0]
    return arr2D
    




if __name__ == '__main__':
    print(f([[1,2],[3,4]]))
    print(f([[1,2,3,4],[5,6,7,8]]))