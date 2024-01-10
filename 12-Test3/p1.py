def f(word):
    if word:
        letters = list(word)
        x = 0
        arr=[]
        while x < (len(letters)+1):
            for i in range(0,len(letters)):
                if i == (x):
                    arr.append((letters[i]).upper())
                else:
                    arr.append((letters[i]).lower())
            x+= 1
        answer = []
        y = len(word)
        for i in range(0,len(arr)-y,y):
            word = ''.join(arr[i:(i+y)])
            answer.append(word)
        return '-'.join(answer)
    else:
        return ''

    

print(f('BOOK'))
    


            
