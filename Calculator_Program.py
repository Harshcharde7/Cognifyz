def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

def modulus(x, y):
    if y == 0:
        return "Cannot calculate modulus with zero"
    else:
        return x % y

def calculator():
    print("\n\t\tSimple Calculator")
    num1 = float(input("\n\t\tEnter the first number: "))
    num2 = float(input("\t\tEnter the second number: "))

    operation = input("\n\t\tEnter the operation (+, -, *, /, %): ")

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    elif operation == '%':
        result = modulus(num1, num2)
    else:
        result = "Invalid operator"

    print(f"\n\t\tResult: {result}\n")

if __name__ == "__main__":
    calculator()
