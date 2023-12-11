import json

movie = {
    "title":"Hachi",
    "year": 2004,
    "actor":{"leading":"Julie","supporting":"Folkerts"},
    "oscar":False,
    "genre": "sad",
    "rating": 9.5,
    "times watched": 3
}
file_name = "favourite.json"

with open(file_name, 'w') as file:
    json.dump(movie, file, indent=4)

with open(file_name, 'r') as file:
    content = json.load(file)
    print(json.dumps(content, indent=4))
