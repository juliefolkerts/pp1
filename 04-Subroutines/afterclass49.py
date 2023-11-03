def f(dice):
    current_count = 1
    max_count = 0
    for i in range(1, len(dice)):
        if dice[i] == dice[i-1]:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 1
    return max_count

result = f('5233165554211')
print(result)
