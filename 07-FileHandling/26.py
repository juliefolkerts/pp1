import re

message = 'To be, or not to be, that is the question'
vouls = re.findall('[aeiou]', message)

amount_vouls = len(vouls)

print(amount_vouls)