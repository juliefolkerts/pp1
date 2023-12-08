def rand_elem(array):
    import random
    index = random.randint(0,len(array)-1)
    result = array[index]
    return result

array = [1,2,3,4,5,6,7,8,9]
print(rand_elem(array))