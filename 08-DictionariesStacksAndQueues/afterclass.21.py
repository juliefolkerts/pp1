import csv
import json
data = [['Product','Quantity','Price'],
    ['milk',8,4.25],
    ['cheese',5,17.90],
    ['bread',21,6.15],
    ['juice',12,5.90]
]
name = 'Products.csv'
with open(name, mode ='w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open(name, mode='r') as file:
    read = csv.reader(file)
    for row in read:
        print(row)


namejson = 'Products.json'
data = []
with open(name, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

with open(namejson, mode= 'w') as file:
    json.dump(data, file, indent=2)

with open(namejson, mode='r') as file:
    reader = json.load(file)
    print(reader)
