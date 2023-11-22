def month(n):
    monthnames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec']
    index = int(n) - 1
    return monthnames[index]

result = [1, 9, 12]
for x in result:
    print(month(x))
