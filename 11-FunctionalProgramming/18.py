values = [48,47,54,50,42,68,39,46]

to_high = lambda speed: speed > 50
result = list(filter(to_high,values))

print('Speed too high:',','.join(map(str,result)))

