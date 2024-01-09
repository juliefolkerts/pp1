bottles = [508,500,512,499,492,511,503,476,501,509]

def tolerance(size):
    maximum = size*1.02
    minimum = size*0.98
    return lambda measurement:minimum>measurement or measurement>maximum

lst = list(filter(tolerance(500),bottles))
result = len(lst)/len(bottles)*100
print(f'incorrectly filled:{int(result)}%')




