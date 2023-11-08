def f(product_code):
    sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    fourth_digit = (sum % 7)
    if fourth_digit != int(product_code[3]):
        return False
    return True

result = f('1114')
print(result)