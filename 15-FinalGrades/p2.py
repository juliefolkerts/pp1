from collections import Counter

def f(arr):
    count_dict = Counter(arr)

    for num, count in count_dict.items():
        if count % 2 == 0:
            return num

# Test case
arr = [6, 6, 6, 6, 4, 5, 2, 2, 2, 2, 2]
print(f(arr))  # Output: 6