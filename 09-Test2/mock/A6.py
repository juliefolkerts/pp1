def f(time):
    arrtime = list(time)
    hour = str(arrtime[0])+str(arrtime[1])
    if int(hour) > 12:
        hour = int(hour) - 12
        if int(hour) < 10:
            hour = f'0{int(hour)}'
    else:
        hour = hour
    arrhour = list(str(hour))
    arrtime[0],arrtime[1] = arrhour[0], arrhour[1]
    result = ''.join(arrtime)
    return result
time = '23:05'
print(f(time))