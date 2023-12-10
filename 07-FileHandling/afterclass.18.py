input_file = 'input.txt'
output_file = 'copy.txt'

with open(input_file, 'r') as input:
    content = input.read()

with open(output_file, 'w') as output:
    output.write(content)