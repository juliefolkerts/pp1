number_products = int(input('Enter number of products:'))
price_product = float(input('Enter price of product:'))
if number_products <= 2:
    print(f'Amount to pay: {number_products * price_product}')
else:
    print(f'Amount to pay: {(number_products - 2) * price_product * 0.75 + (2 * price_product)}')