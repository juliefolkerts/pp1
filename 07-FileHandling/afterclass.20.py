with open('MeatAndFish.txt', 'w') as file:
    file.write('Skinless white meat\n')
    file.write('Tuna fish\n')
    file.write('Luncheon meat\n')
    file.write('Lean cuts of red meat\n')

with open('GrainsAndBread.txt', 'w') as file:
    file.write('Bread\n')
    file.write('Rice\n')
    file.write('All purpose flour\n')
    file.write('Pasta\n')

with open('MeatAndFish.txt', 'r') as file:
    content1 = file.read()

with open('GrainsAndBread.txt', 'r') as file:
    content2 = file.read()

with open('allproducts.txt', 'w') as file:
    file.write(content1)
    file.write('\n')
    file.write(content2)

with open('allproducts.txt', 'r') as file:
    print(file.read())

