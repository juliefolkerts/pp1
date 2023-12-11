import json

with open("myJsonFile0.json") as file:
    data = json.load(file)

for key,value in data.items():
    print(f"{key} : {value}")
