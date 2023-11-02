def f(number1, number2, number3):
    if number1 < number2 and number1 < number3:
        smallest_n = number1
    elif number2 < number1 and number2 < number3:
        smallest_n = number2
    elif number3 < number1 and number3 < number2:
        smallest_n = number3
    else:
        print('at least 2 of the numbers have the same value')
    if number1 > number2 and number1 > number3:
        biggest_n = number1
    elif number2 > number1 and number2 > number3:
        biggest_n = number2
    elif number3 > number1 and number3 > number2:
        biggest_n = number3
    else:
        print('at least 2 of the numbers have the same value')
    return (int(biggest_n) - int(smallest_n))

result = f(2, 12, 8)
print(result)
    
