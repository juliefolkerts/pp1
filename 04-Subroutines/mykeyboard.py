def read_number(x,y):
    return x + y

number1 = int(input('Enter number:\n'))
number2 = int(input('Enter number:\n'))
if __name__ == '__main__':
    print(f'{number1} + {number2} = {read_number(number1, number2)}')