def f(d):
    in_park = set()
    
    for car, action in d:
        if action == "in":
            in_park.add(car)
        elif action == "out" and car in in_park:
            in_park.remove(car)

    result = sorted(list(in_park))
    return result

if __name__ == '__main__':
    cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"], ["BA111","in"],["BA123","out"],["KR234","in"]]
    print(f(cars))
    cars1 = [["KR234","in"],["KR234","out"]]
    print(f(cars1))

