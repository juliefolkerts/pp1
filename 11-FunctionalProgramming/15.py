text = 'I completely agree with you'

words = text.split()
count_letters = lambda word: len(word)
result =list(map(count_letters,words))
print(f'No. of letters in words:{result}')