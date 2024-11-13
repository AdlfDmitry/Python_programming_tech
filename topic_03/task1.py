def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    return "Unable to divide by zero"
def calculator():
    while True:  
        num1_input = input("Enter first number ('exit' to quit): ")
        if num1_input.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break  
        try:
            num1 = float(num1_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        num2_input = input("Enter second number: ")
        try:
            num2 = float(num2_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue  
        operation = input("Choose operator (+, -, *, /): ")
        match operation:
            case '+':
                print("Result: ", add(num1, num2))
            case '-':
                print("Result:", subtract(num1, num2))
            case '*':
                print("Result:", multiply(num1, num2))
            case '/':
                print("Result:", divide(num1, num2))
            case _:
                print("Unknown operator. Please try again.")
calculator()
