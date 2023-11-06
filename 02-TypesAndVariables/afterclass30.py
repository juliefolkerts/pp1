import random
dice = int(random.randrange(1,7))
print(f'Dice rolled:{dice}')
if ((dice == 1) or (dice == 6)) :
    print('Special number: True')
else:
    print('Special number: False')