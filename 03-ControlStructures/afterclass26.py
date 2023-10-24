# car_speed
# speed_limit_min
# speed_limit_max
car_speed = float(input('Enter car speed:'))
speed_limit_min = int(40)
speed_limit_max = int(140)
if car_speed > speed_limit_max or car_speed < speed_limit_min:
    print('Invalid car speed!')