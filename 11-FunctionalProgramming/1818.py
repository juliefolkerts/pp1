limit = lambda x: x > 50
speeds = [48,47,54,50,42,68,39,46]

result = list(filter(limit,speeds))
print(f'recorded values:48,47,54,50,42,68,39,46')
print(f'Speed to high:{','.join(map(str,result))}')