amount_paid = float(input('Enter amount paid:'))
VAT = (float(amount_paid * 0.23))
print(f'Amount:{amount_paid}')
rounded_VAT = round(VAT, 2)
print(f'VAT:{rounded_VAT}')
