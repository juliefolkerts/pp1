test_results = [
    {"name":"Peter","result":27},
    {"name":"Anna","result":63},
    {"name":"Robert","result":92},
    {"name":"Paul","result":46},
    {"name":"Barbara","result":52}]

points = lambda dic: 70>dic['result']>50
people = list(filter(points,test_results))
for x in people:
    print(f'{x['name']}')