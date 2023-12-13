text = 'An apple a day keeps the doctor away'
arr_letters = list(text)
arr_words = text.split()

def a(text):
    arr_words = text.split()
    result = len(arr_words)
    return result

def b(text):
    arr_words = text.split()
    new_arr = []
    for i in range(0,len(arr_words)):
        for j in range(0, len(arr_words)-i-1):
            if len(arr_words[j]) < len(arr_words[j+1]):
                arr_words[j], arr_words[j+1] = arr_words[j+1], arr_words[j]
    return arr_words

def c(text):
    lower_case = text.lower()
    arr_words = lower_case.split()
    sort_words = sorted(arr_words)
    return sort_words

print(a(text))
print(b(text))

#chatgpt answer for c
original_list = ['An', 'a', 'apple', 'away', 'day', 'doctor', 'keeps', 'the']
sorted_list = sorted(arr_words, key=lambda s: s.lower())

print(sorted_list)