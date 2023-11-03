def f(product_code):
    a = int(product_code[0])
    b = int(product_code[1])
    c = int(product_code[2])
    d = int((a + b + c) % 7)
    if int(product_code[3]) == d:
        return True
    else:
        return False

result = f('1114')
print(result)