def f(player1, player2):
    player1 = list(player1)
    player2 = list(player2)
    score_1 = 0
    score_2 = 0
    for i in range(0,len(player1)):
        if player1[i] == 'A' or player1[i] == 'K' or player1[i] ==  'Q' or player1[i] ==  'J' or player1[i] ==  'T':
            score_1 += 10
        else:
            score_1 += int(player1[i])
    for i in range(0,len(player2)):
        if player2[i] == 'A' or player2[i] == 'K' or player2[i] ==  'Q' or player2[i] ==  'J' or player2[i] ==  'T':
            score_2 += 10
        else:
            score_2 += int(player2[i])
    if score_1 >= score_2:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))
    