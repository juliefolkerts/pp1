import random
dice = int(random.randrange(1,6))
print(f'Dice rolled:{dice}')
if ((dice == 1) or (dice == 0)) :
    print('Special number: True')
else:
    print('Special number: False')