def f(amount_to_pay):
    amount_to_pay = int(amount_to_pay)
    PLN5 = int(amount_to_pay / 5)
    PLN2 = int((amount_to_pay - (PLN5*5)) / 2)
    PLN1 = amount_to_pay - (PLN2*2 + PLN5*5)
    totalcoins = PLN5 + PLN2 + PLN1
    return totalcoins

if __name__ == "__main__":
    print(f(23))
    print(f(8))