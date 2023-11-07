def f(sentence):
    words = sentence.split()
    end = ''.join(words)
    return end

result = f('hey there hwo are you')
print(result)