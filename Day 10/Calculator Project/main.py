from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


# Dictionary mapping operators to functions
operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculation(num1, num2, operator):
    # Directly access the function from the dictionary
    if operator in operation:
        return operation[operator](num1, num2)
    else:
        return "Invalid operator"


def calculator():
    should_continue = True
    num1 = float(input("Enter your 1st number: "))

    while should_continue:
        operator = input("Enter the operator +, -, *, /: ")

        # Check if operator is valid before asking for 2nd number
        if operator not in operation:
            print("Invalid operator. Please try again.")
            continue

        num2 = float(input("Enter your 2nd number: "))

        result = calculation(num1, num2, operator)
        print(f"{num1} {operator} {num2} = {result}")

        next_operation = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if next_operation == 'y':
            num1 = result
        else:
            should_continue = False
            print("\n" * 25)
            calculator()
            return


# Start the calculator
calculator()