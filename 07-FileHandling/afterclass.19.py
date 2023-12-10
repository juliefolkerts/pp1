input_file = 'input.txt'
output_file = 'copylines.txt'

with open(input_file, 'r') as input:
    lines = input.readlines()

with open(output_file, 'w') as output:
    for line in lines:
        output.write(line)