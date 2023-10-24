#washing_product = "shoes"
#rinse = True
#spin = False
#Total washing time: 35 minutes
washing_product = input('Enter type of product:')
if washing_product == 'shoes':
    washing_product = int(20)
elif washing_product == 'jacket':
    washing_product = int(40)
elif washing_product == 'underwear':
    washing_product = int(70)
rinse = True
spin = False
if rinse == True:
    rinse = int(15)
elif rinse == False:
    rinse = int(0)
if spin == True:
    spin = int(9)
elif spin == False:
    spin = int(0)
washing_time = (int(washing_product) + (rinse) + (spin))
print(f'Total washing time:{washing_time}')