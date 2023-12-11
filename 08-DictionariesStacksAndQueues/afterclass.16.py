def hotel_list(hotels):
    list_hotels = []
    for hotel in hotels:
        list_hotels.append(hotel["name"])
    return list_hotels

def avg_price(hotels):
    total = 0
    for hotel in hotels:
        x = int(hotel["price"])
        total += x
    avg = total / len(hotels)
    return int(avg)

Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

def cheapest(x,y):
    if avg_price(x) < y:
        return x
    else:
        return y


print(f'Hotels in Krakow: {hotel_list(Hotels_in_Krakow)}')
print(f'Average hotel price in Krakow:{avg_price(Hotels_in_Krakow)}')
print(f'Hotels in Sopot: {hotel_list(hotels_in_Sopot)}')
print(f'Average hotel price in Sopot:{avg_price(hotels_in_Sopot)}')
print(f'Cheaper hotels in: {cheapest(avg_price(Hotels_in_Krakow),avg_price(hotels_in_Sopot))}')

