def display_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    total_lines = len(lines)
    
    for i in range(0,total_lines, 5):
        print(''.join(lines[i:(i+5)]).strip())
        input()

filename = 'movies.txt'
print(display_lines(filename))