from operations import get_number, get_operator, execute_operation
from log import makeLog

def calculator():
    while True:
        try:
            num1 = get_number("Enter first number ('exit' to quit): ")
            if num1 is None:  
                break
            num2 = get_number("Enter second number: ")
            if num2 is None: 
                break
            operation = get_operator()
            result = execute_operation(num1, num2, operation)
            print(f"Result: {result}")
            makeLog(num1, operation, num2, result)

        except ZeroDivisionError as e:
            print(f"Error: Division by zero is not allowed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator()
