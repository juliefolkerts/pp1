import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)  #if you do double \\ the warning won't be printed
total = 0
print(temperatures)
for x in temperatures:
    total += int(x)

average = total / len(temperatures)
print(int(average))
