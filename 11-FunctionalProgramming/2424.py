grades = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
    return lambda pts: pts>=limit

result = list(filter(min_pts(70),grades))
print(f'Min 70 pts:{result}')
b = list(filter(min_pts(40),grades))
print(f'Min 40 pts:{b}')
c = list(filter(min_pts(30),grades))
print(f'Min 30 pts:{c}')

