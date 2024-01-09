test_results = [
    {"name":"Peter","result":27},
    {"name":"Anna","result":63},
    {"name":"Robert","result":92},
    {"name":"Paul","result":46},
    {"name":"Barbara","result":52}]

a = list(filter(lambda x:70 > x['result'] > 50, test_results))
students = []
for x in a:
    students.append(x['name'])

print(', '.join(students))