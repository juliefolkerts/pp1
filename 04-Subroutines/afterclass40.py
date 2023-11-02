def f(number):
    str_number = str(number)
    for digit in str_number:
        if str_number.count(digit) > 1:
            sum_digit = int(digit) * str_number.count(digit)
            return sum_digit
    return '0'

result = f('230335')
print(result)