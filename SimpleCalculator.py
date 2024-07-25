# Define a function for each operation
def add(x, y):
    """Return the sum of x and y"""
    return x + y

def subtract(x, y):
    """Return the difference of x and y"""
    return x - y

def multiply(x, y):
    """Return the product of x and y"""
    return x * y

def divide(x, y):
    """Return the quotient of x and y"""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y

def main():
    # Prompt the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt the user to choose an operation
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter the number of your chosen operation: ")

    # Perform the selected operation and display the result
    if choice == "1":
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
        print("the result is",result)
    elif choice == "2":
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
        print("the result is",result)
    elif choice == "3":
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
        print("the result is",result)
    elif choice == "4":
        try:
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
            print("the result is",result)
        except ZeroDivisionError as e:
            print(e)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()