def f(card_number):
    card_number = str(card_number)
    return f'{card_number[0:2]}**********{card_number[-4:]}'


print(f("5290312400019022"))