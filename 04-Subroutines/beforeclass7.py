#Define an anonymous function that calculates the body mass index (BMI) for the 
#given weight in kg and height in cm. Then, calculate the BMI for Peter (81kg, 182cm). 
#Sample result:
#Peter’s BMI is …
BMI = lambda w, h: w // h**2
print(BMI(81, 1.82))
