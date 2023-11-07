def f(number, even):
    if even == True:
        number = str(number)
        sumeven = 0
        for i in range(0, len(number)):
            if int(number[i]) % 2 == 0:
                sumeven += int(number[i])
            else:
                sumeven = sumeven
        return sumeven
    else:
        number = str(number)
        sumodd = 0
        for i in range(0, len(number)):
            if int(number[i]) % 2 != 0:
                sumodd += int(number[i])
            else:
                sumodd = sumodd
        return sumodd

if __name__ == "__main__":    
    result = f(13115,True)
    print(result)


        