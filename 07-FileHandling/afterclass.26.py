import re
text = 'To be, or not to be, that is the question'

count = 0
vouls = re.findall(r'[aeoui]', text) #don't need the r'
for voul in vouls:
    count += 1
print(count)