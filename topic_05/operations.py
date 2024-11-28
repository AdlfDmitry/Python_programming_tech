from functions import add, subtract, multiply, divide
def get_number(prompt):
    while True:
        num_input = input(prompt)
        if num_input.lower() == 'exit':
            return None
        try:
            return float(num_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operator():
    while True:
        operation = input("Choose operator (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        print("Unknown operator. Please choose from (+, -, *, /).")

def execute_operation(num1, num2, operation):
    match operation:
        case '+':
            return add(num1, num2)
        case '-':
            return subtract(num1, num2)
        case '*':
            return multiply(num1, num2)
        case '/':
            return divide(num1, num2)
