def f(c):
    count = 0
    cards = list(c)
    for i in range(0,len(cards)):
        if cards[i] == 'A' or cards[i] == 'K' or cards[i] == 'Q' or cards[i] == 'J' or cards[i] == 'T':
            count += 10
        else:
            count += int(cards[i])
    return count

if __name__ == '__main__':
    c1 = '2K9'
    c2 = '234AJ7'
    print(f(c1))
    print(f(c2))