current_price = float(input('Current product price:'))
previous_price = float(input('Previous product price:'))
reduction = (100 - ((current_price / previous_price) * 100))
if reduction >= 10:
    print('Buy the product!!')
    print(f'Product price reduced by {reduction}%')
