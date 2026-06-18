# This calculator was built with AI assistance
import math


def square_root(num):
    """Calculate the square root of a number."""
    if num < 0:
        return "Error: Cannot calculate square root of negative number"
    return math.sqrt(num)


def calculate(num1, num2, operator):
    """Perform calculation based on operator."""
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else "Error: Division by zero",
        '**': num1 ** num2,
        '%': num1 % num2 if num2 != 0 else "Error: Division by zero"
    }
    return operations.get(operator, "Error: Invalid operator")


def main():
    print("=" * 40)
    print("        TERMINAL CALCULATOR")
    print("=" * 40)
    print("Operators: +  -  *  /  **  %  sqrt")
    print("Type 'quit' to exit\n")

    while True:
        try:
            user_input = input("Enter first number: ").strip()
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break

            num1 = float(user_input)

            operator = input("Enter operator (+, -, *, /, **, %, sqrt): ").strip()
            if operator.lower() == 'quit':
                print("Goodbye!")
                break

            if operator.lower() == 'sqrt':
                result = square_root(num1)
                print(f"\n>>> sqrt({num1}) = {result}\n")
            else:
                num2 = float(input("Enter second number: ").strip())
                result = calculate(num1, num2, operator)
                print(f"\n>>> {num1} {operator} {num2} = {result}\n")

        except ValueError:
            print("Error: Please enter valid numbers.\n")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()

