import random
dice_1 = int(random.randrange(1,7))
dice_2 = int(random.randrange(1,7))
dice_3 = int(random.randrange(1,7))

print(f"{dice_1}")
print(f"{dice_2}")
print(f"{dice_3}")

sum_dices = dice_1 + dice_2 + dice_3
print(F'Sum of dice rolled: {sum_dices}')