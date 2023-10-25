#6
def computepay(hours, rate):
    if hours > 40:
        pay = (hours - 40)*rate*1.5 + 40 * rate
    else:
        pay = hours * rate
    return pay

hours = int(input("Enter hours: "))
rate = float(input("Enter rate: "))
pay = computepay(hours, rate)
print("Pay: ", pay)
#7
def computegrade(grade):
    if grade < 0 or grade > 1.0:
        return "Score is out of range!"
    elif grade >= 0.9:
        return "A"
    elif grade >= 0.8:
        return "B"
    elif grade >= 0.7:
        return "C"
    elif grade >= 0.6:
        return "D"
    else:
        return "F"


try:
    grade = float(input("Enter score: "))
except:
    print("Bad score")
    quit()

print(computegrade(grade))