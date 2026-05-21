# Calculator Program

# Addition function
def addition(a, b):
    return a + b


# Subtraction function
def subtraction(a, b):
    return a - b


# Multiplication function
def multiplication(a, b):
    return a * b


# Division function
def division(a, b):
    if b == 0:
        return "Division by zero is not possible!"
    return a / b


# Main menu using while loop
while True:
    print("\n===== CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice in ["1", "2", "3", "4"]:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", addition(num1, num2))

        elif choice == "2":
            print("Result:", subtraction(num1, num2))

        elif choice == "3":
            print("Result:", multiplication(num1, num2))

        elif choice == "4":
            print("Result:", division(num1, num2))

    elif choice == "5":
        print("Calculator closed.")
        break

    else:
        print("Invalid choice! Please try again.")