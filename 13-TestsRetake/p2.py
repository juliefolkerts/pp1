def f(x, y, d):
    for num in range(x, y + 1):
        num_str = str(num)
        if d in num_str:
            return True

    return False



if __name__ == '__main__':
    print(f(10, 15, "14"))  
    print(f(100, 120, "11"))  
    print(f(205, 210, "04"))


