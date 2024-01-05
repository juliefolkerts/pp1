stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]

value = lambda product: (product[0])*(product[1])
result = sum(list(map(value,stock)))
print(result)