average_speed = lambda x,y,z: x / (z/60 + y)

distance = float(input('Enter km:'))
hours = int(input('enter hours:'))
minutes = int(input('enter minutes:'))

print(f'speed:{average_speed(distance,hours,minutes):.1f}')