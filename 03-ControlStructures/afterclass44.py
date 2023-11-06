def f():
    sum = 0
    quanity = 0
    while True:
        x = int(input('Enter number:'))
        sum += x
        quanity += 1
        if x == 0:
            break
    mean = sum / (quanity-1)
    result = print(f'RESULT: Quantity={quanity-1}, Sum={sum}, Mean={mean}')

f()
