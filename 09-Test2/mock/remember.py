import csv
import json


with open('text.csv', mode='r') as file:
    reader = csv.DictReader(file)
    print(reader)

with open('text.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open('text.json', mode='r') as file:
    content = json.load(file)

with open('text.json', mode='w', indent=4) as file:
    json.dump(data, file)

x = thisdict.get('key3', None)
for x in thisdict.keys():
    x khhjhhjg

x = dict1.update(dict2)

import matplotlib.pyplot as plt
import numpy as np
x = np.array[]
y = np.array[]
plt.plot(x,y, marker line color)
plt.show()

import re
pattern = re.compile(sdfsdf)
if pattern.match(text):
    
