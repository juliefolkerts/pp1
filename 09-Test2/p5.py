import re
with open('data.txt', 'r') as file:
    content = file.read()

def f(first, last):
    count = 0
    x = re.findall(fr'\b[{first}]\w*[{last}]\b', content)
    result = len(x)
    return result

