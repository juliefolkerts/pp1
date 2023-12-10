import csv

data = [
    ["first_name", "last_name", "age", "gender", "email"],
    ["Decca", "Blackstone", 52, "Male", "dblackstone0@time.com"],
    ["Elena", "Rechert", 27, "Female", "erechert1@ucoz.com"],
    ["Bibbye", "Norree", 26, "Female", "bnorree2@reddit.com"],
    ["Alasdair", "McCoole", 53, "Male", "amccoole3@foxnews.com"],
    ["Hogan", "Hatrey", 26, "Male", "hhatrey4@zimbio.com"]
]

with open('students.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open('students.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row['age']) < 30:
            print(f'{row['first_name']} {row['last_name']} {row['email']}')