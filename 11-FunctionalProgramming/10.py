def avg_speed(distance,hours,minutes):
    hrs = (minutes/60) + hours
    speed = distance / hrs
    return (speed)


distance = float(input('Enter km:'))
hours = int(input('enter hours:'))
minutes = int(input('enter minutes:'))
print(f'{avg_speed(distance,hours,minutes):.1f}')