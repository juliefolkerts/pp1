from stack import stack as Stack

def dec_to_bin(dec_number):
    my_stack = Stack()  # Create an instance of the Stack class
    dec_number = int(dec_number)

    # Push all remainders onto the stack
    while dec_number > 0:
        remainder = dec_number % 2
        my_stack.push(remainder)
        dec_number = dec_number // 2

    bin_number = ''
    while not my_stack.empty():
        bin_number += str(my_stack.pop())
    return bin_number

dec_number = input('Enter decimal number:')
print(dec_to_bin(dec_number))
