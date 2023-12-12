from stack import push, pop, empty, display

def calculate_rpn(expression):
    operators = set(['+', '-', '*', '/'])
    stack = []

    for token in expression:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            push(float(token))
        elif token in operators:
            if len(stack) < 2:
                print("Invalid RPN expression. Not enough operands for operator:", token)
                return None
            else:
                operand2 = pop()
                operand1 = pop()
                result = perform_operation(operand1, operand2, token)
                push(result)
        else:
            print("Invalid RPN expression. Unknown token:", token)
            return None

    if not empty():
        return pop()
    else:
        print("Invalid RPN expression. Stack is empty.")
        return None

def perform_operation(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            print("Error: Division by zero.")
            return None
        else:
            return operand1 / operand2

# Get input from the user for RPN expression
rpn_input = input("Enter RPN expression (space-separated): ")
expression_tokens = rpn_input.split()

# Calculate RPN expression
result = calculate_rpn(expression_tokens)

# Display the result
if result is not None:
    print("Result:", result)