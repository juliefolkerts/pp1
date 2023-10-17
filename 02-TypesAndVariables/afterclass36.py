selling_rate = float(input('Bank sells:\n'))
buying_rate = float(input('Bank buys:\n'))
spread = selling_rate - buying_rate
print('Spread:', round(spread, 5))