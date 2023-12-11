import json

student_data = {
    "name": "John Doe",
    "age": 20,
    "gender": "Male",
    "grades": {"math": 85, "english": 92, "history": 78},
    "is_active": True,
    "hobbies": ["reading", "coding", "sports"],
    "address": {
        "street": "123 Main Street",
        "city": "Anytown",
        "state": "CA",
        "zip_code": "12345",
    },
}

file_name = "student.json"

with open (file_name, 'w') as file:
    json.dump(student_data, file, indent=4)

with open (file_name, 'r') as file:
    data = json.load(file)
    print(json.dumps(data, indent=1))