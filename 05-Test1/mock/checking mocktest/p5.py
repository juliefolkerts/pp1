def f(binary_number):
    binary_number = str(binary_number)
    for i in range(0, len(binary_number)):
        if (binary_number[i] != '0') and (binary_number[i] != '1'):
            return False
    return True

if __name__ == "__main__":  
    print(f('101101'))