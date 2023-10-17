guess = int(input('Enter guess:\n'))
import random
dice = int(random.randrange(1,6))
if (guess == dice):
    print('True')
else:
    print('False')