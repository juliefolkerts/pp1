i = 1
sum = 0
for i in range(1,11):
    if i % 2 == 0:
        print(i)
        sum += i
print(f'sum of even numbers: {sum}')