arr = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
    return lambda pts: pts>=limit

a = min_pts(70)
print(list(filter(a,arr)))
