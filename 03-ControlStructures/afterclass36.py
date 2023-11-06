def multtable(x):
    for i in range(1,11):
        print(f'{x} x {i} = {x*i}')

a = int(input('Enter number:'))
result = multtable(a)
print(result)