def rectanglestar(a, b):
    print(b * '*')
    for i in range(2, a):
        print('*',((b-4)*' '),'*')
    print(b * '*')

result = rectanglestar(5, 17)
print(result)
