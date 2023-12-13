
def f(arr):
    num_count = {}
    for num in arr:
        if num in num_count:
            num_count[num]+=1
        else:
            num_count[num] = 1
    unique_num = [num for num in num_count if num_count[num]==1]
    return unique_num


arr = [2,3,2,5,8,1,9,8]

print(f'unique items:{f(arr)}')