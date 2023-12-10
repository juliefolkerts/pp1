movie_titles = ['1', '2', '33', '4', '6', '77777']
with open('movies.txt', 'w') as file:
    for movie in movie_titles:
        file.write(movie)
        file.write('\n')

with open('movies.txt', 'r') as file:
    print(file.read())