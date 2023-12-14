def f(player1, player2):
    arr1 = list(player1)
    arr2 = list(player2)
    count1 = 0
    for i in range(0,len(arr1)):
        if arr1[i] == 'A' or arr1[i] == 'K' or arr1[i] == 'Q' or arr1[i] == 'J' or arr1[i] == 'T':
            count1 += 10
        else:
            count1+= int(arr1[i])
    count2 = 0
    for i in range(0,len(arr2)):
        if arr2[i] == 'A' or arr2[i] == 'K' or arr2[i] == 'Q' or arr2[i] == 'J' or arr2[i] == 'T':
            count2 += 10
        else:
            count2+= int(arr2[i])
    if count1 >= count2:
        result = True
    else:
        result = False
    return result

if __name__ == '__main__':
    player1 = 'AJ972'
    player2 = 'AQT72'
    print(f(player1,player2))
    player1 = '9532'
    player2 = 'K8'
    print(f(player1,player2))
