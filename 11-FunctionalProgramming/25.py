dic = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

positives = lambda city: dic[city] > 0
print(list(filter(positives, dic)))