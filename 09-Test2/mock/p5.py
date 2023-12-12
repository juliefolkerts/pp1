import re
with open('data.txt', 'r') as file:
    content = file.read()


def f(first_letter,last_letter):
    first_letter = str(first_letter)
    last_letter = str(last_letter)
    words = re.findall(f'(^[{first_letter}]) ($[{last_letter}])', content)
    return len(words)

print(f('w', 'd'))

