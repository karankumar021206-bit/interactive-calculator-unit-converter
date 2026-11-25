
def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                print("Result:", num1 + num2)
            elif operator == "-":
                print("Result:", num1 - num2)
            elif operator == "*":
                print("Result:", num1 * num2)
            elif operator == "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero")
                else:
                    print("Result:", num1 / num2)
            else:
                print("Invalid operator!")

        except ValueError:
            print("Invalid input! Please enter numbers.")

        again = input("Calculate again? (yes/no): ").lower()
        if again != "yes":
            break


def unit_converter():
    while True:
        print("\n--- Unit Converter ---")
        print("1. KM to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                km = float(input("Enter kilometers: "))
                print("Miles:", km * 0.621371)

            elif choice == 2:
                c = float(input("Enter Celsius: "))
                print("Fahrenheit:", (c * 9/5) + 32)

            elif choice == 3:
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a valid number!")


while True:
    print("\n===== Interactive Calculator =====")
    print("1. Calculator")
    print("2. Unit Converter")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            calculator()
        elif choice == 2:
            unit_converter()
        elif choice == 3:
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")
