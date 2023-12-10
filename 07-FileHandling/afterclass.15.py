with open('filename.txt', 'w') as file:
     file.write('hello')


with open('filename.txt', 'r') as file:
     print(file.read())
