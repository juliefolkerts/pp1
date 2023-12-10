import re

with open('grades.txt', 'w') as file:
    file.write('Name: Peter')
    file.write('Grades: 3.5, 4.0, 5.0, 4.5, 3.5, 3.0, 5.0')

with open('grades.txt', 'r') as file:
    content = file.read()

grades = re.findall(r'\d.\d', content)
total = 0
for grade in grades:
    total += float(grade)

average = total / len(grades)

print(average)