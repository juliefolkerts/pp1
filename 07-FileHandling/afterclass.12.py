# define personal data
name = "Julie Folkerts"
university = "Krakow University of Economics"
field = "Applied Informatics"

# write to a file
with open('student.txt', 'w') as file:
    file.write(name+"\n")
    file.write(university+'\n')
    file.write(field+'\n')
    file.close()

file = open('student.txt','r')
file_content = file.read()
print( file_content )
file.close()


