def f(card):
    arr = list(card)
    value = {
        'A' : 1,
        'K' : 13,
        'Q' : 12,
        'J' : 11,
        'T' : 10,
        '9' : 9,
        '8' : 8,
        '7' : 7,
        '6' : 6,
        '5' : 5,
        '4' : 4,
        '3' : 3,
        '2' : 2,
    }
    for i in range(0,len(arr)):
        for j in range(0,i-1):
            if value[str(arr[j])] < value[str(arr[i])]:
                arr[j], arr[i] = arr[i], arr[j]
    result = ''
    for x in arr:
        result+= x
    result = ''
    for x in arr:
        result+= x
    return result
card = "T9JK3"
print(f(card))