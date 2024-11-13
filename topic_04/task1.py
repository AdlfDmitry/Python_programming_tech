def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:  
        raise ZeroDivisionError("Unable to divide by zero")
    else:  
     return a / b
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
        else:
            print("Unknown operator. Please choose from (+, -, *, /).")
def calculator():
    while True:
        num1 = get_number("Enter first number ('exit' to quit): ")
        if num1 is None:
            print("Exiting...")
            break
        num2 = get_number("Enter second number: ")
        if num2 is None:
            print("Exiting...")
            break    
        operation = get_operator()     
        match operation:
            case '+':
                print("Result:", add(num1, num2))
            case '-':
                print("Result:", subtract(num1, num2))
            case '*':
                print("Result:", multiply(num1, num2))
            case '/':
                print("Result:", divide(num1, num2))
calculator()
