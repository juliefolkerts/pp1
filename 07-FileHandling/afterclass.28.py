import re

with open('file.txt', 'w') as file:
    file.write('Hello, evhifh, odofjgjjjjj fj fohrsd jjjjjjjjjj')

with open('file.txt', 'r') as file:
    content = file.read()

words = re.findall(r'\b\w{6,}\b', content)
for word in words:
    print(word)