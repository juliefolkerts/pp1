import json

with open('data,json', mode='r') as file:
    content = json.load(file)

def f(years, course):
    years = int(years)
    count = 0
    for student in content:
        if int(student["age"]) >= years:
            for data in student["studies"]["courses"]:
                if data["name"] == course and sum(data["grades"])/len(data[ "grades"]) >= 4:
                    count += 1
