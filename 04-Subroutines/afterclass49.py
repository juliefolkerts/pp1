def f(dice):
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    for i in range(1, len(dice)):
        if dice[i] == 1 and dice[i-1] == 1:
            count1 += 1
        else:
            count1 = 1
        if dice[i] == 2 and dice[i-1] == 2:
            count2 += 1
        else:
            count2 = 1
        if dice[i] == 3 and dice[i-1] == 3:
            count3 += 1
        else:
            count3 = 1
        if dice[i] == 4 and dice[i-1] == 4:
            count4 += 1
        else:
            count4 = 1
        if dice[i] == 5 and dice[i-1] == 5:
            count5 += 1
        else:
            count5 = 1
        if dice[i] == 6 and dice[i-1] == 6:
            count6 += 1
        else:
            count6 = 1
    if max(count1, count2, count3, count4, count5, count6) == count1:
        x = 1
    elif max(count1, count2, count3, count4, count5, count6) == count2:
        x = 2
    elif max(count1, count2, count3, count4, count5, count6) == count3:
        x = 3
    elif max(count1, count2, count3, count4, count5, count6) == count4:
        x = 4
    elif max(count1, count2, count3, count4, count5, count6) == count5:
        x = 5
    else:
        x = 6
    return x

result = f('5233165554211')
print(result)
