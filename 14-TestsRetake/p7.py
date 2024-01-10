def f(product_code):
    result = False
    lst = list(product_code)
    sum = int(lst[0])+int(lst[1])+int(lst[2])
    answer = sum%7
    if len(product_code) == 4:
        if int(lst[3]) == answer:
            result = True
    return result

if __name__ == '__main__':
    print(f('704'))