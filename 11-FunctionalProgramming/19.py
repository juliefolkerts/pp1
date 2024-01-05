grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

good_grades = lambda grade: grade > 2.0

mean = sum(list(filter(good_grades,grades)))/len(list(filter(good_grades,grades)))

print(f'{mean:.2f}')