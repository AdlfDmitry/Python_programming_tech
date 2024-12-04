from calculator import Calculator

def get_user_input():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return a, b
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return None

def main():
    calc = Calculator()
    
    while True:
        print("\nCalculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Choose an operation (1-5): ")
        if choice == "5":
            print("Exiting")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Wrong choice")
            continue

        values = get_user_input()
        if values is None:
            continue
        
        a, b = values
        
        try:
            if choice == "1":
                result = calc.add(a, b)
            elif choice == "2":
                result = calc.subtract(a, b)
            elif choice == "3":
                result = calc.multiply(a, b)
            elif choice == "4":
                result = calc.divide(a, b)
            
            print(f"Result: {result}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
