measurements = [508,500,512,499,492,511,503,476,501,509]

def f(mills,tollerance):
    minimum = mills * ((100-tollerance)/100)
    maximum = mills * ((100+tollerance)/100)
    return lambda amount: maximum >= amount >= minimum

x = f(500,2)
good_ones = list(filter(x,measurements))

print('Bottle capacity:    500ml')
bad_ones = 100 - (len(good_ones)/len(measurements)*100)
print(f'{int(bad_ones)}%')