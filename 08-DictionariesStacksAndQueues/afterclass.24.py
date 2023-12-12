from stack import push, pop, empty, display

# Function to convert decimal to binary using stack
def decimal_to_binary(decimal):
    while decimal > 0:
        remainder = decimal % 2
        push(remainder)
        decimal //= 2

# Get input from the user
decimal_number = int(input("Enter a decimal number: "))

# Convert decimal to binary using the stack
decimal_to_binary(decimal_number)

#bin_number = ''
#while not my_stack.empty():
    #bin_number += str(my_stack.pop())
#return bin_number
# Display the binary representation
print("Binary representation:")
while not empty():
    print(pop(), end="")
print()


