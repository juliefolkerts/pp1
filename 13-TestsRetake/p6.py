import re

def f(mnumbers):
    count = 0
    for nr in mnumbers:
        pattern = re.compile(r'^[1-7+-a-dA-D][a-dA-D1-7]*$')
        if pattern.match(nr):
            count+=1
        else:
            count = count
    return count

if __name__ == '__main__':
    print(f(['A15','-31','7abC', '+D1','-gH']))
