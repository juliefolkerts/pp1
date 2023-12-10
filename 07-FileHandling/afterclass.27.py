import re
text = 'To be, or not to be, that is the question'

spaces = re.findall('\s',text)
count = 1
for space in spaces:
    count += 1

print(count)