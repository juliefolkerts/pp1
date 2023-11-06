guess = int(input('Enter guess:\n'))
import random
dice = int(random.randrange(1,7))
print(dice)
if (guess == dice):
    print('True')
else:
    print('False')