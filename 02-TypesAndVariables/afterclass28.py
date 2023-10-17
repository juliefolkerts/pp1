weight = float(input('Enter your weight in kg:\n'))
height = float(input('Enter height in meter:\n'))
BMI = float(weight / (height) ** 2) #18.5 till 24.9
if ((BMI >= 18.5) and (BMI <= 24.9)) :
    print('Healthy weight: True')
else:
    print('Healthy weight: False')