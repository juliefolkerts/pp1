# 1, 2 and 5 PLN
# defide by 5 first, if amount%5 = 0, th
def f(amount_to_pay):
    PLN5 = int(amount_to_pay // 5)
    PLN2 = int((amount_to_pay - PLN5 * 5) // 2)
    PLN1 = amount_to_pay - (PLN5 * 5) - (PLN2 * 2)
    return (PLN5 + PLN2 + PLN1)

amount_to_pay = 23
print(f(amount_to_pay))