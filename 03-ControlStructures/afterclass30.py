time_24_format = input('Enter time in 24 hour format:\n')
print(f'Time in 12 hour format: {int(time_24_format[:2]) - 12}:{(time_24_format[3:])}pm')