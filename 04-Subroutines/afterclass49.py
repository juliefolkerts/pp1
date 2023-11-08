def f(dice):
    current_count = 1
    for x in range(1, 7):
        for i in range(1, len(dice)):
            if dice[i] == x and dice[i-1] == x:
                current_count += 1
            else:
                current_count = 1

result = f('5233165554211')
print(result)
